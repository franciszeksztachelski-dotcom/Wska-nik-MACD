"""Część podstawowa projektu MACD: wczytanie danych, wskaźnik i symulacja."""

from pathlib import Path
import sys

import pandas as pd

from plots import save_all_figures

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

DATA_PATH = Path(__file__).resolve().parent / "AAPL.csv"
FIGURES_DIR = Path(__file__).resolve().parent / "figures"
N1, N2, N3 = 12, 26, 9
START_IDX = 100
SIGNAL_FROM = 101
DELAY = 1  # transakcja w próbce i + 1 po cenie x_{i+1}


def load_prices(path: Path) -> pd.DataFrame:
    """Wczytaj CSV i zweryfikuj dane wejściowe zgodnie z p. 3.1."""
    data = pd.read_csv(path, parse_dates=["date"])
    required = {"date", "close"}
    missing = required - set(data.columns)
    if missing:
        raise ValueError(f"Brak wymaganych kolumn: {sorted(missing)}")

    data = data.sort_values("date").reset_index(drop=True)

    if data["date"].duplicated().any():
        raise ValueError("Wykryto zduplikowane daty.")
    if data["close"].isna().any() or data["date"].isna().any():
        raise ValueError("Wykryto braki w datach lub cenach zamknięcia.")
    if (data["close"] <= 0).any():
        raise ValueError("Ceny zamknięcia muszą być dodatnie.")
    if not (1000 <= len(data) <= 1200):
        raise ValueError(
            f"Liczba obserwacji L={len(data)} wykracza poza zakres 1000–1200."
        )
    return data


def compute_macd(
    close: pd.Series, n1: int = N1, n2: int = N2, n3: int = N3
) -> pd.DataFrame:
    """Oblicz EMA, MACD, SIGNAL, histogram i sygnały kupna/sprzedaży."""
    ema_fast = close.ewm(span=n1, adjust=False).mean()
    ema_slow = close.ewm(span=n2, adjust=False).mean()
    macd = ema_fast - ema_slow
    signal = macd.ewm(span=n3, adjust=False).mean()
    histogram = macd - signal

    prev_h = histogram.shift(1)
    buy = (prev_h <= 0) & (histogram > 0)
    sell = (prev_h >= 0) & (histogram < 0)

    trade_signal = pd.Series(0, index=close.index, dtype=int)
    trade_signal = trade_signal.mask(buy, 1)
    trade_signal = trade_signal.mask(sell, -1)
    trade_signal.iloc[0] = 0

    return pd.DataFrame(
        {
            "ema_fast": ema_fast,
            "ema_slow": ema_slow,
            "macd": macd,
            "signal": signal,
            "histogram": histogram,
            "trade_signal": trade_signal,
        }
    )


def simulate_macd(
    close: pd.Series, trade_signal: pd.Series, delay: int = DELAY
) -> tuple[pd.DataFrame, list[dict]]:
    """Symulacja transakcji MACD (p. 3.2–3.4)."""
    n = len(close)
    cash = pd.Series(pd.NA, index=close.index, dtype="Float64")
    qty = pd.Series(pd.NA, index=close.index, dtype="Float64")
    equity = pd.Series(pd.NA, index=close.index, dtype="Float64")

    cash.iloc[START_IDX] = 1000.0 * close.iloc[START_IDX]
    qty.iloc[START_IDX] = 0.0
    equity.iloc[START_IDX] = cash.iloc[START_IDX]

    closed_trades: list[dict] = []
    open_buy: dict | None = None

    for i in range(START_IDX + 1, n):
        cash.iloc[i] = cash.iloc[i - 1]
        qty.iloc[i] = qty.iloc[i - 1]

        signal_idx = i - delay
        if signal_idx >= SIGNAL_FROM:
            sig = int(trade_signal.iloc[signal_idx])
            price = float(close.iloc[i])
            prev_cash = float(cash.iloc[i - 1])
            prev_qty = float(qty.iloc[i - 1])

            if sig == 1 and prev_cash > 0:
                qty.iloc[i] = prev_cash / price
                cash.iloc[i] = 0.0
                open_buy = {
                    "buy_idx": i,
                    "buy_signal_idx": signal_idx,
                    "buy_price": price,
                }
            elif sig == -1 and prev_qty > 0:
                cash.iloc[i] = prev_qty * price
                qty.iloc[i] = 0.0
                if open_buy is not None:
                    ret = 100.0 * (price / open_buy["buy_price"] - 1.0)
                    closed_trades.append(
                        {
                            **open_buy,
                            "sell_idx": i,
                            "sell_signal_idx": signal_idx,
                            "sell_price": price,
                            "return_pct": ret,
                        }
                    )
                    open_buy = None

        equity.iloc[i] = cash.iloc[i] + qty.iloc[i] * close.iloc[i]

    portfolio = pd.DataFrame({"cash": cash, "position_qty": qty, "equity": equity})
    return portfolio, closed_trades


def print_summary(
    data: pd.DataFrame,
    portfolio: pd.DataFrame,
    closed_trades: list[dict],
) -> None:
    start_cash = float(portfolio["cash"].iloc[START_IDX])
    final_equity = float(portfolio["equity"].iloc[-1])
    portfolio_return = 100.0 * (final_equity / start_cash - 1.0)
    profitable = [t for t in closed_trades if t["return_pct"] >= 0]
    losing = [t for t in closed_trades if t["return_pct"] < 0]
    n_closed = len(closed_trades)
    win_pct = 100.0 * len(profitable) / n_closed if n_closed else float("nan")
    open_qty = float(portfolio["position_qty"].iloc[-1])

    print(f"Instrument: AAPL")
    print(f"Obserwacje L: {len(data)}")
    print(f"Zakres dat: {data['date'].iloc[0].date()} – {data['date'].iloc[-1].date()}")
    print(f"Parametry: MACD({N1}, {N2}, {N3}), d={DELAY}")
    print(f"Kapitał początkowy C[{START_IDX}]: {start_cash:.2f} USD")
    print(f"Wartość końcowa V[{len(data) - 1}]: {final_equity:.2f} USD")
    print(f"Stopa zwrotu portfela R: {portfolio_return:.2f} %")
    print(f"Transakcje zamknięte: {n_closed}")
    print(f"  zyskowne: {len(profitable)}")
    print(f"  stratne: {len(losing)}")
    if n_closed:
        print(f"Udział zyskownych: {win_pct:.2f} %")
        print(
            f"Największy zysk: {max(t['return_pct'] for t in closed_trades):.2f} %"
        )
        print(
            f"Największa strata: {min(t['return_pct'] for t in closed_trades):.2f} %"
        )
    print(
        "Pozycja otwarta na końcu:"
        f" {'tak' if open_qty > 0 else 'nie'} (Q={open_qty:.6f})"
    )


def main() -> None:
    data = load_prices(DATA_PATH)
    indicator = compute_macd(data["close"])
    portfolio, closed_trades = simulate_macd(
        data["close"], indicator["trade_signal"]
    )
    result = pd.concat([data, indicator, portfolio], axis=1)
    print_summary(data, portfolio, closed_trades)
    save_all_figures(result, closed_trades, FIGURES_DIR)
    print(f"Wykresy zapisano w: {FIGURES_DIR}")


if __name__ == "__main__":
    main()
