"""Wykresy A1–E2 części podstawowej (grafika wektorowa PDF)."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

START_IDX = 100
SIGNAL_FROM = 101

BUY_COLOR = "#2ca02c"
SELL_COLOR = "#d62728"
MACD_COLOR = "#1f77b4"
SIGNAL_COLOR = "#ff7f0e"
PRICE_BG = "#bdbdbd"
HIST_POS = "#4caf50"
HIST_NEG = "#e57373"

BUY_MARKER = "^"
SELL_MARKER = "v"


def _style_time_axis(ax) -> None:
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    ax.set_xlabel("Data")
    ax.grid(True, alpha=0.3)


def _scatter_signals(ax, dates, values, mask, *, color, marker, label, filled=True, size=70, zorder=5):
    if not mask.any():
        return
    facecolors = color if filled else "none"
    ax.scatter(
        dates[mask],
        values[mask],
        marker=marker,
        s=size,
        c=facecolors,
        edgecolors=color,
        linewidths=1.4,
        label=label,
        zorder=zorder,
    )


def plot_a(df: pd.DataFrame, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df["date"], df["close"], color="#1f77b4", linewidth=1.4, label="Cena zamknięcia")
    ax.axvspan(
        df["date"].iloc[0],
        df["date"].iloc[START_IDX],
        color="0.85",
        label="Zakres bez transakcji (próbki 0–100)",
        zorder=0,
    )
    start = df["date"].iloc[0].date()
    end = df["date"].iloc[-1].date()
    ax.set_title(f"A1. Cena zamknięcia AAPL [USD], {start} – {end}")
    ax.set_ylabel("Cena zamknięcia [USD]")
    _style_time_axis(ax)
    ax.legend(loc="upper left")
    fig.tight_layout()
    fig.savefig(path, format="pdf")
    plt.close(fig)


def plot_b(df: pd.DataFrame, path: Path) -> None:
    fig, ax_price = plt.subplots(figsize=(12, 6))
    ax_ind = ax_price.twinx()

    (line_price,) = ax_price.plot(
        df["date"],
        df["close"],
        color=PRICE_BG,
        linewidth=1.0,
        zorder=1,
        label="Cena zamknięcia (lewa oś)",
    )
    (line_macd,) = ax_ind.plot(
        df["date"],
        df["macd"],
        color=MACD_COLOR,
        linewidth=1.8,
        zorder=3,
        label="MACD (prawa oś)",
    )
    (line_signal,) = ax_ind.plot(
        df["date"],
        df["signal"],
        color=SIGNAL_COLOR,
        linewidth=1.8,
        zorder=3,
        label="SIGNAL (prawa oś)",
    )

    ax_price.set_title("B1. Cena zamknięcia oraz MACD i SIGNAL — AAPL")
    ax_price.set_ylabel("Cena zamknięcia [USD]")
    ax_ind.set_ylabel("MACD, SIGNAL [USD]")
    _style_time_axis(ax_price)
    ax_price.legend(
        [line_price, line_macd, line_signal],
        [line_price.get_label(), line_macd.get_label(), line_signal.get_label()],
        loc="upper left",
    )
    fig.tight_layout()
    fig.savefig(path, format="pdf")
    plt.close(fig)


def plot_c(df: pd.DataFrame, path: Path) -> None:
    view = df.iloc[START_IDX:].copy()
    dates = view["date"]
    buy = (view["trade_signal"] == 1) & (view.index >= SIGNAL_FROM)
    sell = (view["trade_signal"] == -1) & (view.index >= SIGNAL_FROM)

    fig, (ax_c1, ax_c2) = plt.subplots(
        2, 1, figsize=(12, 8), sharex=True, gridspec_kw={"height_ratios": [2, 1]}
    )

    ax_c1.plot(dates, view["macd"], color=MACD_COLOR, linewidth=1.6, label="MACD")
    ax_c1.plot(dates, view["signal"], color=SIGNAL_COLOR, linewidth=1.6, label="SIGNAL")
    _scatter_signals(
        ax_c1, dates, view["macd"], buy, color=BUY_COLOR, marker=BUY_MARKER, label="Kupno"
    )
    _scatter_signals(
        ax_c1, dates, view["macd"], sell, color=SELL_COLOR, marker=SELL_MARKER, label="Sprzedaż"
    )
    ax_c1.set_title("C1. MACD, SIGNAL i sygnały kupna/sprzedaży — AAPL")
    ax_c1.set_ylabel("MACD, SIGNAL [USD]")
    ax_c1.legend(loc="upper left")
    ax_c1.grid(True, alpha=0.3)

    colors = [HIST_POS if h >= 0 else HIST_NEG for h in view["histogram"]]
    ax_c2.bar(dates, view["histogram"], width=1.8, color=colors, label="Histogram $H_i$")
    ax_c2.axhline(0.0, color="black", linewidth=0.8, label="Poziom zero")
    ax_c2.set_title("C2. Histogram MACD $H_i$ — AAPL")
    ax_c2.set_ylabel("Histogram $H_i$ [USD]")
    _style_time_axis(ax_c2)
    ax_c2.legend(loc="upper left")

    fig.tight_layout()
    fig.savefig(path, format="pdf")
    plt.close(fig)


def plot_d(df: pd.DataFrame, trade: dict, path: Path, pad: int = 30) -> None:
    left = max(0, int(trade["buy_idx"]) - pad)
    right = min(len(df) - 1, int(trade["sell_idx"]) + pad)
    view = df.iloc[left : right + 1]

    fig, ax_price = plt.subplots(figsize=(12, 6))
    ax_ind = ax_price.twinx()

    (line_price,) = ax_price.plot(
        view["date"],
        view["close"],
        color=PRICE_BG,
        linewidth=1.2,
        zorder=1,
        label="Cena zamknięcia (lewa oś)",
    )
    (line_macd,) = ax_ind.plot(
        view["date"],
        view["macd"],
        color=MACD_COLOR,
        linewidth=1.8,
        zorder=2,
        label="MACD (prawa oś)",
    )
    (line_signal,) = ax_ind.plot(
        view["date"],
        view["signal"],
        color=SIGNAL_COLOR,
        linewidth=1.8,
        zorder=2,
        label="SIGNAL (prawa oś)",
    )

    buy_sig = df.iloc[int(trade["buy_signal_idx"])]
    sell_sig = df.iloc[int(trade["sell_signal_idx"])]
    buy_exe = df.iloc[int(trade["buy_idx"])]
    sell_exe = df.iloc[int(trade["sell_idx"])]

    ax_price.scatter(
        [buy_sig["date"]],
        [buy_sig["close"]],
        marker=BUY_MARKER,
        s=90,
        facecolors="none",
        edgecolors=BUY_COLOR,
        linewidths=1.6,
        label="Sygnał kupna",
        zorder=5,
    )
    ax_price.scatter(
        [sell_sig["date"]],
        [sell_sig["close"]],
        marker=SELL_MARKER,
        s=90,
        facecolors="none",
        edgecolors=SELL_COLOR,
        linewidths=1.6,
        label="Sygnał sprzedaży",
        zorder=5,
    )
    ax_price.scatter(
        [buy_exe["date"]],
        [buy_exe["close"]],
        marker=BUY_MARKER,
        s=110,
        c=BUY_COLOR,
        edgecolors=BUY_COLOR,
        label="Wykonanie kupna",
        zorder=6,
    )
    ax_price.scatter(
        [sell_exe["date"]],
        [sell_exe["close"]],
        marker=SELL_MARKER,
        s=110,
        c=SELL_COLOR,
        edgecolors=SELL_COLOR,
        label="Wykonanie sprzedaży",
        zorder=6,
    )

    r = trade["return_pct"]
    annotation = (
        f"Kupno: {buy_exe['date'].date()}  {float(buy_exe['close']):.2f} USD\n"
        f"Sprzedaż: {sell_exe['date'].date()}  {float(sell_exe['close']):.2f} USD\n"
        f"Stopa zwrotu r = {r:+.2f} %"
    )
    ax_price.annotate(
        annotation,
        xy=(sell_exe["date"], sell_exe["close"]),
        xytext=(0.62, 0.12),
        textcoords="axes fraction",
        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.9, "edgecolor": "0.6"},
        fontsize=10,
        arrowprops={"arrowstyle": "->", "color": "0.4"},
    )

    ax_price.set_title("D1. Wybrana zamknięta transakcja (największy zysk) — AAPL")
    ax_price.set_ylabel("Cena zamknięcia [USD]")
    ax_ind.set_ylabel("MACD, SIGNAL [USD]")
    _style_time_axis(ax_price)
    handles, labels = ax_price.get_legend_handles_labels()
    handles.extend([line_macd, line_signal])
    labels.extend([line_macd.get_label(), line_signal.get_label()])
    ax_price.legend(handles, labels, loc="upper left")
    fig.tight_layout()
    fig.savefig(path, format="pdf")
    plt.close(fig)


def plot_e(df: pd.DataFrame, closed_trades: list[dict], path: Path) -> None:
    view = df.iloc[START_IDX:].copy()
    dates = view["date"]
    buy_all = (view["trade_signal"] == 1) & (view.index >= SIGNAL_FROM)
    sell_all = (view["trade_signal"] == -1) & (view.index >= SIGNAL_FROM)

    executed_buy_sig = {t["buy_signal_idx"] for t in closed_trades}
    executed_sell_sig = {t["sell_signal_idx"] for t in closed_trades}
    executed_buy_idx = {t["buy_idx"] for t in closed_trades}
    executed_sell_idx = {t["sell_idx"] for t in closed_trades}

    buy_exec_sig = buy_all & view.index.isin(executed_buy_sig)
    sell_exec_sig = sell_all & view.index.isin(executed_sell_sig)
    buy_unexec = buy_all & ~view.index.isin(executed_buy_sig)
    sell_unexec = sell_all & ~view.index.isin(executed_sell_sig)
    buy_exec = view.index.isin(executed_buy_idx)
    sell_exec = view.index.isin(executed_sell_idx)

    fig, (ax_e1, ax_e2) = plt.subplots(
        2, 1, figsize=(12, 8), sharex=True, gridspec_kw={"height_ratios": [2, 1]}
    )

    ax_e1.plot(dates, view["close"], color="#1f77b4", linewidth=1.3, label="Cena zamknięcia")
    _scatter_signals(
        ax_e1,
        dates,
        view["close"],
        buy_exec_sig,
        color=BUY_COLOR,
        marker=BUY_MARKER,
        label="Sygnał kupna (wykonany)",
        filled=True,
        size=55,
    )
    _scatter_signals(
        ax_e1,
        dates,
        view["close"],
        sell_exec_sig,
        color=SELL_COLOR,
        marker=SELL_MARKER,
        label="Sygnał sprzedaży (wykonany)",
        filled=True,
        size=55,
    )
    _scatter_signals(
        ax_e1,
        dates,
        view["close"],
        buy_unexec,
        color=BUY_COLOR,
        marker=BUY_MARKER,
        label="Sygnał kupna (niewykonany)",
        filled=False,
        size=80,
    )
    _scatter_signals(
        ax_e1,
        dates,
        view["close"],
        sell_unexec,
        color=SELL_COLOR,
        marker=SELL_MARKER,
        label="Sygnał sprzedaży (niewykonany)",
        filled=False,
        size=80,
    )
    _scatter_signals(
        ax_e1,
        dates,
        view["close"],
        buy_exec,
        color=BUY_COLOR,
        marker=BUY_MARKER,
        label="Wykonanie kupna",
        filled=True,
        size=110,
        zorder=6,
    )
    _scatter_signals(
        ax_e1,
        dates,
        view["close"],
        sell_exec,
        color=SELL_COLOR,
        marker=SELL_MARKER,
        label="Wykonanie sprzedaży",
        filled=True,
        size=110,
        zorder=6,
    )

    ax_e1.set_title("E1. Cena AAPL z sygnałami wykonanymi i niewykonanymi")
    ax_e1.set_ylabel("Cena zamknięcia [USD]")
    ax_e1.legend(loc="upper left", ncol=2, fontsize=8)
    ax_e1.grid(True, alpha=0.3)

    ax_e2.plot(
        dates,
        view["equity"],
        color="#6a3d9a",
        linewidth=1.6,
        label="Wartość portfela $V_i$",
    )
    ax_e2.set_title("E2. Wartość portfela w czasie — AAPL")
    ax_e2.set_ylabel("Wartość portfela $V_i$ [USD]")
    _style_time_axis(ax_e2)
    ax_e2.legend(loc="upper left")

    fig.tight_layout()
    fig.savefig(path, format="pdf")
    plt.close(fig)


def save_all_figures(
    df: pd.DataFrame, closed_trades: list[dict], output_dir: Path
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    if not closed_trades:
        raise ValueError("Brak zamkniętej transakcji do wykresu D1.")

    best = max(closed_trades, key=lambda t: t["return_pct"])
    plot_a(df, output_dir / "A.pdf")
    plot_b(df, output_dir / "B.pdf")
    plot_c(df, output_dir / "C.pdf")
    plot_d(df, best, output_dir / "D.pdf")
    plot_e(df, closed_trades, output_dir / "E.pdf")
    return output_dir
