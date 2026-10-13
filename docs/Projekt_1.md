Projekt 1. Wskaźnik MACD.
Piotr Sypek
2 października 2026
1 Wstęp
MACD (ang. moving average convergence/divergence) jest wskaźnikiem stosowanym w analizie
technicznej rynków finansowych. Analiza techniczna bada historyczne ceny i inne dane rynkowe,
np. wielkość obrotu, w celu m.in. rozpoznawania trendów i poszukiwania właściwych momentów kupna
i sprzedaży [1, 2]. MACD pomaga oceniać kierunek i dynamikę zmian cen oraz wyznaczać sygnały
wspierające decyzje kupna i sprzedaży instrumentów finansowych [1, 3].
Wskaźnik MACD można wyznaczyć dla danych wejściowych stanowiących kolejne ceny akcji, kursy
walut, notowania kryptowalut, wartości indeksów giełdowych, ceny surowców itp. Wynikiem obliczeń
są dwie krzywe, MACD i SIGNAL. Kierunek ich przecięcia sugeruje właściwy moment kupna lub
sprzedaży, jednakże nie gwarantuje osiągnięcia zysku.
W projekcie 1 głównym celem prac jest przedstawienie obiektywnych cech wskaźnika MACD na
podstawie osiągniętych rezultatów numerycznych, czyli należy poddać analizie zarówno sytuacje, gdy
zastosowanie wskaźnika MACD prowadzi do przeprowadzenia zyskownych, jak i stratnych transakcji.
Źródło danych do przeprowadzenia analizy przydatności wskaźnika MACD ma stanowić program
napisany w Pythonie. W części podstawowej projektu program ten wykonuje symulację operacji
maklerskich, dla których decyzje kupna i sprzedaży realizowane są tylko na podstawie sygnałów
generowanych przez MACD. Program ten wczytuje dane, oblicza wskaźnik, rozpoznaje sygnały, realizuje
operacje kupna i sprzedaży oraz generuje odpowiednie wykresy i podsumowanie wyników.
Algorytm MACD opisano w punkcie 2, symulację w punkcie 3, a wymagane slajdy w punkcie 4.
Korzystanie z narzędzi AI jest wymagane. Mogą one wspierać każdy etap pracy, w tym tworzenie kodu,
analizę rezultatów symulacji i przygotowanie prezentacji.
Można korzystać z dowolnych ogólnodostępnych pakietów i bibliotek Pythona oraz pakietów LaTeX.
Dane wejściowe opracowanego programu powinny stanowić ceny zamknięcia dowolnego aktywa.
Kod do projektu 1 powinien składać się z dwóch głównych części:
• Część podstawowa realizująca obliczenia do podstawowej symulacji (omówienie w p. 3).
• Część eksperymentalna implementująca własne modyfikacje procesu decyzyjnego (p. 5).
2 Algorytm wyznaczania MACD
Pierwszym celem obliczeń jest otrzymanie krzywych MACD i SIGNAL, których przecięcia określają
sugerowane momenty kupna i sprzedaży. MACD porównuje dwie wykładnicze średnie kroczące cen,
reagujące z różną szybkością na ich zmiany. SIGNAL jest wykładniczą średnią kroczącą obliczaną
z wartości MACD i stanowi linię odniesienia dla tego porównania.
2.1 Od cen do krzywych MACD i SIGNAL
Niech L oznacza liczbę obserwacji, i = 0, . . . , L − 1 ich indeks, a xi cenę zamknięcia w próbce i.
Jedna próbka ceny może być określana dla różnego zakresu czasu: jednej minuty, pięciu minut, jednej
godziny, danych dziennych (czas jednej sesji lub jeden dzień notowań, zależnie od rynku), danych
tygodniowych, miesięcznych itp.
Posiadając wektor danych wejściowych x można wyznaczyć wykładniczą średnią kroczącą (ang.
Exponential Moving Average, EMA). EMA jest średnią, w której wpływ starszych cen stopniowo
maleje. Jej okres N oznacza liczbę przedziałów notowań określającą szybkość reakcji średniej, np.
N = 12 oznacza EMA 12-sesyjną dla dziennych danych giełdowych [7]. Symbol E
(N)
i
oznacza wartość
tej średniej, a αN współczynnik wygładzania, czyli wagę bieżącej ceny. Dla okresu N przyjmuje się:
αN =
2
N + 1
, E(N)
0 = x0, E(N)
i = αN xi + (1 − αN )E
(N)
i−1
(i ≥ 1). (1)
1
E
(N)
i
jest zatem wartością EMAN dla próbki o indeksie i. Mniejszy okres N oznacza większą wagę
bieżącej ceny, a nie odrzucanie obserwacji starszych niż N próbek.
Konfigurację wskaźnika zapisuje się jako MACD(N1, N2, N3), gdzie trzy dodatnie parametry całkowite
oznaczają:
• N1 – okres krótszej EMA cen, szybciej reagującej na ich zmiany,
• N2 – okres dłuższej EMA cen, przy czym N1 < N2,
• N3 – okres EMA wartości MACD, wyznaczającej linię SIGNAL.
Symbole Mi
i Si oznaczają odpowiednio wartości MACD i SIGNAL w próbce i dla wybranych
parametrów. Oblicza się je następująco:
Mi = E
(N1)
i − E
(N2)
i
, (2)
S0 = M0, Si = αN3Mi + (1 − αN3
)Si−1 (i ≥ 1). (3)
Współczynnik αN3 = 2/(N3 + 1) wynika z (1). MACD(12,26,9) jest standardowym ustawieniem
często stosowanym przez inwestorów i analityków technicznych [3]. W części podstawowej projektu
należy przyjąć N1 = 12, N2 = 26 i N3 = 9.
Należy obliczyć obie krzywe od pierwszej próbki, zachowując pełną historię średnich. Można korzystać
z pakietów Pythona służących do ich wyznaczenia. W pandas można użyć metody Series.ewm i wywołać
ceny.ewm(span=N, adjust=False).mean(), gdzie ceny to obiekt pandas.Series zawierający kolejne
ceny zamknięcia. Parametr span=N określa okres średniej, a adjust=False zapewnia wyznaczanie
EMA rekurencyjnie, zgodnie ze wzorem (1) [4].
2.2 Sygnały kupna i sprzedaży
Przecięcie linii SIGNAL przez MACD od dołu jest sygnałem kupna, a przecięcie od góry
jest sygnałem sprzedaży [1]. Przykład występowania tych sygnałów przedstawiono na rysunku 1.
W celu wyznaczenia tych sygnałów w programie, można wprowadzić symbol Hi
, który oznacza wartość
histogramu MACD w próbce i, czyli różnicę wartości MACD i SIGNAL:
Hi = Mi − Si
. (4)
Dodatnie Hi oznacza, że MACD znajduje się nad SIGNAL, a ujemne, że MACD znajduje się pod
SIGNAL. Wystąpienie sygnałów można wyznaczyć na podstawie zmiany znaku histogramu dla i ≥ 1:
• sygnał kupna wystąpi w próbce i, gdy Hi−1 ≤ 0 i Hi > 0,
• sygnał sprzedaży wystąpi w próbce i, gdy Hi−1 ≥ 0 i Hi < 0,
• brak nowego sygnału w próbce i, gdy Hi = 0.
Sygnał przypisuje się pierwszej próbce po przejściu na drugą stronę linii SIGNAL, bez interpolowania
czasu przecięcia.
100 110 120 130 140 150 160 170 180 190 200 210 220
−1
0
1
2
Indeks próbki i
Wartość wskaźnika [USD]
Przecięcia MACD i SIGNAL
MACD SIGNAL Kupno Sprzedaż
Rysunek 1: MACD i SIGNAL obliczone dla syntetycznych cen akcji hipotetycznej spółki notowanej w dolarach
amerykańskich (USD). Znaczniki wskazują sygnały rozpoznane w kolejnych próbkach.
2
Histogram MACD zwykle przedstawia wartości Hi jako słupki względem poziomu zero. Ułatwia to
dostrzeżenie zmian odległości między krzywymi MACD i SIGNAL [1]. Słupki zbliżające się do zera
wskazują zbliżanie się MACD i SIGNAL. Histogram MACD należy umieścić w części podstawowej
prezentacji i krótko omówić w trakcie prezentacji.
2.3 Świece i wykres świecowy
Świeca przedstawia cztery ceny z jednego przedziału notowań, np. godziny lub sesji:
• cenę otwarcia,
• cenę zamknięcia,
• cenę najwyższą,
• cenę najniższą.
Korpus świecy rozciąga się między ceną otwarcia a ceną zamknięcia. Końce cienkich linii, zwanych
cieniami, wskazują najwyższą i najniższą cenę [1]. Często świeca spadkowa (cena zamknięcia mniejsza
od ceny otwarcia) rysowana jest kolorem czerwonym, natomiast świeca wzrostowa kolorem zielonym [11].
Na prezentacji można przedstawić dane wejściowe jako wykres świecowy. Wymaga to pobrania
wszystkich czterech cen dla każdego przedziału. Do obliczeń MACD i symulacji nadal wykorzystuje się
ceny zamknięcia. Przykład świec przedstawiono na rysunku 2.
10:00 11:00
94
98
102
106
110
114
Otwarcie: 110
Zamknięcie: 104
Zamknięcie: 100
Otwarcie: 96
Czas
Cena [USD]
Rysunek 2: Dwie kolejne świece na przykładowym wykresie godzinowym instrumentu finansowego notowanego
w dolarach amerykańskich (USD). Godziny na osi czasu oznaczają czas pomiaru ceny otwarcia.
Zauważ, że choć druga świeca jest zielona, jej cena zamknięcia (100 USD) jest niższa od ceny zamknięcia
pierwszej świecy (104 USD). Jest to przykład, że świeca wzrostowa ilustruje wzrost ceny zamknięcia
względem ceny otwarcia dla tego samego przedziału czasu, a nie ceny zamknięcia poprzedniej świecy.
2.4 Czas realizacji transakcji
Transakcja oznacza pojedynczą operację kupna lub sprzedaży instrumentu finansowego. Otwarta
pozycja to posiadany instrument, którego nie sprzedano. W rzeczywistym handlu można reagować na
zmiany wskaźnika w dowolnym czasie sesji. Należy jednak pamiętać, że dopóki świeca się kształtuje,
bieżąca cena i obliczane z niej wartości MACD i SIGNAL mogą się zmieniać. Może to doprowadzić do
sytuacji, w której przecięcie MACD i SIGNAL może pojawić się w trakcie budowania aktualnej świecy
i zniknąć przed jej zamknięciem. Z tego względu sygnał obliczany z ceny zamknięcia można potwierdzić
dopiero po zakończeniu świecy. Jeśli decyzję opiera się wyłącznie na zakończonych świecach, transakcję
na podstawie sygnału z próbki i można wykonać najwcześniej w przedziale odpowiadającym próbce
i + 1. Na potrzeby tego projektu można wybrać jeden z dwóch wariantów obliczeń (sugerowane jest
wybranie wariantu pierwszego, ale wariant drugi nie zostanie uznany za błędny):
• Wykonanie transakcji w próbce i + 1, po cenie xi+1. Decyzja korzysta z już znanego sygnału,
co lepiej odpowiada kolejności zdarzeń w realnym handlu na podstawie zakończonych świec.
• Wykonanie transakcji w próbce i, po cenie xi. Pozwala zbadać uproszczony wariant realizacji
transakcji po cenie zamknięcia próbki, w której rozpoznano sygnał. Jest jednak uproszczeniem:
końcowa cena zamknięcia i sygnał obliczony z tej ceny nie są znane w trakcie budowy świecy. Może
to prowadzić do przypisania transakcji ceny, której nie dałoby się uzyskać po rozpoznaniu sygnału,
i zawyżać wynik symulacji.
3
W profesjonalnym teście strategii decyzję opiera się na informacjach dostępnych w chwili składania
zlecenia. Jeśli sygnał wymaga ostatecznej ceny zamknięcia, jest znany dopiero po zakończeniu świecy.
Pierwszy wariant obliczeń zachowuje tę kolejność, dlatego lepiej odpowiada praktyce inwestycyjnej.
Jednak realizacja transakcji z ceną xi+1 również stanowi uproszczenie: oznacza wykonanie transakcji
według ceny następnego zamknięcia. Ponieważ zastosowanie ceny otwarcia dla i + 1 świecy wymagałoby
operowania na dodatkowym wektorze danych, to przy realizacji części podstawowej należy ograniczyć
obliczenia do zastosowania jednego z powyżej opisanych uproszczonych wariantów obliczeń.
Zastosowanie alternatywnych wobec przedstawionych powyżej wariantów określenia ceny transakcji
można zastosować w części eksperymentalnej. W takiej sytuacji do oceny wpływu takich zmian
należałoby się odnieść do rezultatów otrzymanych bez przeprowadzenia wybranych modyfikacji.
3 Część podstawowa projektu 1
3.1 Dane wejściowe
W części podstawowej należy przygotować wektor zawierający od 1000 do 1200 kolejnych cen
zamknięcia wybranego instrumentu lub indeksu, zapisanych wraz z datami w pliku tekstowym
lub CSV. Dane mają być uporządkowane od najstarszych do najnowszych, dodatnie, bez braków
i duplikatów dat. Przerw między sesjami nie należy uzupełniać sztucznymi cenami. Należy podać
instrument, jednostkę, źródło, zakres dat oraz informację o korektach cen, np. z tytułu podziału akcji.
W dalszym opisie przyjęto L = 1001 elementów, czyli indeksy 0, . . . , 1000, dla wektora cen i
wektorów stanu portfela. Opracowany w ramach projektu program należy dostosować do faktycznej
liczby obserwacji L: ostatni indeks 1000 występujący w opisie należy wówczas zastąpić przez L − 1.
W projekcie można zastosować dowolne dane wejściowe, które zostały pobrane w formacie cvs. Dane
można wybrać m.in. z następujących bezpłatnych źródeł:
• notowania spółek i indeksów z warszawskiej giełdy: https://stooq.pl/, np. PKO BP, indeks WIG20.
Dane pobiera się w sekcji „Dane historyczne”, w formacie CSV.
• Surowce: https://stooq.pl/, np. cena złota w USD za uncję XAUUSD. Przy pobieraniu notowań
surowców należy sprawdzić, czy wybrane dane dotyczą ceny surowca, czy kontraktu terminowego.
• indeksy z USA: Nasdaq Composite, Nasdaq-100 i S&P 500. Przycisk Download umożliwia wybór
CSV.
• Kryptowaluty: Binance Public Data, rynek spot, dane klines, interwał 1d. Z plików CSV należy
odczytać daty i ceny Close, zgodnie z opisem kolumn.
Do pobrania danych wejściowych można użyć również inne źródła. Przy pobieraniu i przygotowaniu
danych z pomocą AI należy zweryfikować ich poprawność, np. porównując wykres z zaufanym
serwisem dla tego samego instrumentu i okresu oraz sprawdzając wybrane daty i ceny.
Do obliczeń można zastosować również wybrane notowania zapisane w udostępnionym w ramach tego
projektu pliku zawierającym notowania wielu spółek z Nasdaq.
3.2 Portfel i zapis jego stanu
Wartość portfela to suma gotówki i bieżącej wartości posiadanego instrumentu finansowego. Należy
utworzyć trzy wektory o długości L, takiej jak długość wektora cen (w opisie L = 1001), zapisujące
stan początkowy w próbce 100 oraz stan po wykonaniu operacji w kolejnych próbkach:
• C – gotówka, element Ci odpowiada cash[i],
• Q – liczba posiadanych jednostek, element Qi odpowiada position_qty[i],
• V – wartość portfela, element Vi odpowiada equity[i].
Nazwy cash, position_qty i equity są to przykładowe nazwy, które można modyfikować we własnym
kodzie. Przebieg wartości portfela oblicza się ze wzoru:
Vi = Ci + Qixi
. (5)
Początkowa gotówka wynosi C100 = 1000x100. W próbce 100 przyjmuje się Q100 = 0 i V100 = C100.
Próbka ta określa stan początkowy, bez wykonywania transakcji. Elementy wektorów C, Q i V o
indeksach 0, . . . , 99 nie są wykorzystywane w symulacji ani na wykresie wartości portfela. W modelu
4
pomija się prowizje, podatki, odsetki, dywidendy oraz inne koszty i wpływy. Dopuszcza się ułamkową
liczbę jednostek, bez sprzedaży instrumentu, którego nie ma w portfelu.
3.3 Algorytm symulacji transakcji MACD
Należy zachować parametry (12, 26, 9) przez całą symulację. Symbol d oznacza opóźnienie wykonania:
d = 0 dla transakcji w próbce sygnału albo d = 1 dla transakcji w następnej próbce (punkt 2.4).
Algorytm obejmuje następujące kroki:
1. Dla wszystkich cen x0, . . . , x1000 obliczyć EMA, MACD, SIGNAL i wartości histogramu. Próbki
0, . . . , 99 służą rozpoczęciu obliczeń średnich, a próbka 100 ustaleniu stanu początkowego portfela.
Sygnały kupna i sprzedaży należy uwzględniać od próbki 101. Pierwszy rozpatrywany
sygnał wyznacza się z H100 i H101.
2. Utworzyć wektory C, Q, V i ustawić ich elementy początkowe zgodnie z punktem 3.2. Kolejno
przetwarzać próbki i = 101, . . . , 1000.
3. Jeżeli i − d ≥ 101, sprawdzić sygnał z próbki i − d. Przy sygnale kupna i Ci−1 > 0 kupić za
całą gotówkę: Qi = Ci−1/xi
, Ci = 0. Przy sygnale sprzedaży i Qi−1 > 0 sprzedać całą pozycję:
Ci = Qi−1xi
, Qi = 0. Jeżeli nie wykonuje się transakcji, także gdy i − d < 101, wartości Ci
i Qi
pozostają takie jak w poprzedniej próbce.
4. Po wyznaczeniu Ci oraz Qi obliczyć Vi według (5). Zapisać indeks sygnału oraz indeks i cenę, przy
której wykonano transakcję.
5. Określić listę transakcji zamkniętych wraz z cenami zakupu i sprzedaży (p. 3.4).
Model zakłada pełne zaangażowanie dostępnego kapitału przy kupnie oraz zamknięcie całej
pozycji przy sprzedaży. Dla d = 1 sygnału z próbki 1000 nie wykonuje się, ponieważ brakuje następnej
ceny.
3.4 Stopa zwrotu i wyniki transakcji
Symbol R oznacza stopę zwrotu całego portfela, czyli procentową zmianę jego wartości względem
początkowej gotówki C100:
R = 100 
V1000
C100
− 1

%. (6)
Jedna zamknięta transakcja oznacza w tej instrukcji parę rzeczywiście wykonanego kupna i późniejszej
sprzedaży całej pozycji. Symbole a i b oznaczają indeksy wykonania odpowiednio kupna i sprzedaży,
a r – stopę zwrotu zamkniętej transakcji, czyli procentowy zysk lub stratę względem kwoty
przeznaczonej na zakup. Przy pominięciu kosztów i dodatkowych wpływów wynosi ona:
r = 100 
xb
xa
− 1

%. (7)
Dla każdej zamkniętej transakcji należy obliczyć stopę zwrotu. Na potrzeby zestawienia w projekcie
transakcje z r ≥ 0 zalicza się do zyskownych (łącznie z transakcjami z r = 0), a z r < 0 do
stratnych. Nie trzeba osobno podawać liczby transakcji o zerowej stopie zwrotu.
W podsumowaniu symulacji należy podać liczbę transakcji zyskownych i stratnych oraz jaki procent
transakcji zamkniętych stanowiły transakcje zyskowne. Otwartej pozycji nie uwzględnia się w tej
statystyce, lecz jej wycena wpływa na stopę zwrotu portfela R. Do części podstawowej należy wybrać
dane pozwalające uzyskać co najmniej jedną zamkniętą transakcję. Jeżeli takich transakcji nie
ma dla wybranych danych wejściowych, to należy zmienić dane wejściowe.
4 Prezentacja wyników części podstawowej
4.1 Slajd tytułowy i wstęp
Slajd tytułowy powinien zawierać temat projektu, imię i nazwisko autora oraz informację, czy jest
to prezentacja wstępna, czy końcowa. Około trzech kolejnych slajdów powinno wyjaśniać, czym
jest MACD, do czego służy i jak się go oblicza. Należy zamieścić równania definiujące EMA, MACD i
SIGNAL oraz wyjaśnić znaczenie zastosowanych symboli. Wstęp ma przedstawiać ogólne znaczenie
algorytmu, bez omawiania każdego szczegółu. Można wskazać źródła informacji, np. literaturę dotyczącą
analizy technicznej.
5
4.2 Wymagane slajdy z wynikami
Poniższy układ obejmuje sześć slajdów wynikowych oznaczonych literami A–F. Wykresy
oznacza się literą slajdu i kolejnym numerem: np. C1 to pierwszy wykres na slajdzie C, a C2 – drugi.
Oznaczenia te uzupełniają numerację stron prezentacji, np. 8/12. Najważniejsze obserwacje związane
z analizą konkretnego wykresu powinny zostać umieszczone na tym samym slajdzie co wykres lub na
następujących po nim slajdach.
A. Dane wejściowe – wykres A1. Wykres ceny dla wszystkich L próbek, z nazwą instrumentu,
jednostką i zakresem dat. Można zastosować wykres liniowy cen zamknięcia lub wykres świecowy,
opisany w punkcie 2.3. Można zaznaczyć początkowy zakres 0, . . . , 100, w którym nie uwzględnia
się sygnałów w symulacji.
B. Cena i wskaźnik – wykres B1. Na wspólnej osi czasu należy przedstawić cenę jasną linią w tle,
a MACD i SIGNAL – wyraźnymi liniami na pierwszym planie. Wartości ceny należy odczytywać na
lewej osi pionowej, a wartości MACD i SIGNAL – na prawej. Opisy osi i legenda muszą jednoznacznie
przypisywać każdą serię do właściwej osi. Przecięcia ceny z liniami wskaźnika nie mają znaczenia
sygnałów kupna ani sprzedaży.
C. Sygnały i histogram – wykresy C1 i C2. U góry (C1) należy przedstawić MACD i SIGNAL z
zaznaczonymi sygnałami kupna i sprzedaży, a poniżej (C2) histogram wartości Hi z poziomem zero.
W trakcie prezentacji należy krótko omówić interpretację wybranej cechy histogramu. Wykresy
mają wspólny zakres czasu, opcjonalnie bez pierwszych 100 próbek. Do próbki 100 włącznie nie
oznacza się sygnałów.
D. Wybrana transakcja – wykres D1. Powiększenie fragmentu wykresu B1 powinno obejmować
faktyczne kupno, następującą po nim sprzedaż oraz otoczenie wcześniejszych i późniejszych próbek.
Na krzywej ceny należy zaznaczyć momenty wykonania kupna i sprzedaży oraz odpowiadające im
sygnały. Należy podać daty i ceny obu operacji oraz wynik procentowy zamkniętej transakcji, czyli
stopę zwrotu r z (7). Należy wyjaśnić, jak zachowanie MACD doprowadziło do tej transakcji. Do
analizy należy wybrać transakcję, która została zarówno otwarta, jak i zamknięta w symulacji. Jeśli
dla wybranych danych nie wystąpiła taka para kupno–sprzedaż, to należy zmienić dane wejściowe.
E. Cała symulacja – wykresy E1 i E2. U góry (E1) należy przedstawić cenę z sygnałami kupna i
sprzedaży oraz odróżnić sygnały wykonane od niewykonanych. Dla d = 1 można rozróżnić moment
sygnału i wykonania transakcji. Na dole (E2) należy przedstawić wartość portfela Vi w funkcji
czasu. Wykresy E1 i E2 powinny mieć wspólny zakres osi czasu, który można rozpocząć od próbki
0 lub 100 (opcja sugerowana). Jeśli oś zaczyna się od próbki 0, zakres 0, . . . , 99 na wykresie E2
pozostaje pusty (wartości portfela sprzed próbki 100 nie należy przedstawiać).
F. Podsumowanie liczbowe i wnioski. Slajd powinien zawierać informacje wymienione w punkcie 4.4
oraz wniosek o działaniu MACD dla badanego instrumentu.
4.3 Slajdy obowiązkowe
Przy opracowywaniu prezentacji należy pamiętać o elementach obowiązkowych opisanych w zasadach
zaliczenia projektu. W szczególności każda prezentacja powinna zawierać trzy kategorie slajdów:
1. wstęp z opisem wskaźnika MACD,
2. slajdy dotyczące zauważonych błędów AI lub deklarację ich niewykrycia,
3. slajdy opisujące konfigurację recenzenta AI oraz rezultat jego uruchomienia.
Brak slajdów obowiązkowych skutkować będzie brakiem zaliczenia prezentacji aż do czasu jej poprawy.
Samo wykonanie poprawy pracy nie powoduje dodatkowego potrącenia punktów. Potrącenia za
nieterminowe oddanie plików lub wygłoszenie prezentacji, ich limity i pozostałe warunki określa punkt
4.1 zasad zaliczenia.
4.4 Zawartość podsumowania liczbowego
Należy podać:
1. kapitał początkowy C100 i końcową wartość portfela V1000,
2. całkowity zysk lub stratę kwotowo oraz stopę zwrotu portfela R w procentach,
3. liczbę zamkniętych transakcji zyskownych (łącznie z transakcjami o zysku równym zero) i stratnych,
6
4. procent transakcji zyskownych wśród wszystkich zamkniętych transakcji,
5. największą procentową stratę w pojedynczej zamkniętej transakcji,
6. największy procentowy zysk w pojedynczej zamkniętej transakcji,
7. informację o ewentualnej pozycji otwartej na końcu symulacji.
Największa strata dotyczy jednej pary kupno–sprzedaż. Jeśli najgorsza transakcja miała stopę
zwrotu −8%, należy podać „największa strata: 8%”. Gdy nie było strat lub zysków, odpowiednią
pozycję należy oznaczyć jako „nie dotyczy”.
4.5 Cechy prawidłowo przygotowanego wykresu
• Tytuł określa przedstawianą wielkość i instrument.
• Każda oś ma opis i jednostkę. Oś czasu wskazuje daty lub indeksy próbek.
• Legenda objaśnia linie, słupki i znaczniki. Kupno i sprzedaż różnią się zarówno kolorem, jak i
kształtem symbolu.
• Wykres z dwiema osiami Y wyraźnie przypisuje przedstawione dane do osi.
• Tekst, grubość linii i wielkość znaczników są czytelne na slajdzie.
• Dane na wykresach, w opisach transakcji i w podsumowaniu liczbowym pochodzą z tego samego
przebiegu programu i tych samych ustawień.
• Format pliku, który zawiera wykres wygenerowany przez program Python, powinien do prezentacji
danych stosować grafikę wektorową (np. PDF, EPS, SVG), a nie rastrową (np. JPG, PNG).
5 Część eksperymentalna: modyfikacje procesu decyzyjnego
Celem jest zbadanie metod ograniczenia wad handlu według algorytmu symulacji transakcji MACD.
Można sprawdzić jeden lub wiele pomysłów, dowolnie modyfikując program. Ocenia się uzasadnienie,
porównanie i interpretację rezultatów symulacji. Również nieskuteczna modyfikacja algorytmu może
otrzymać pełną punktację za poprawną analizę i prezentację rezultatów.
W tej części projektu nie ma nakładanych ograniczeń na modyfikację algorytmu, lecz występuje
obowiązek zastosowania w obliczeniach zestawu danych wejściowych opisanych w p. 5.2.
5.1 Przykładowe kierunki eksperymentów
• Dodatkowe warunki decyzji – kierunek zalecany. Można zbadać, czy generacja sygnałów
kupna i sprzedaży wyznaczona przy zastosowaniu innych metod ogranicza transakcje stratne
i zwiększa zyski. Przykładem jest zastosowanie wskaźnika RSI [1, rozdz. 10]. Alternatywą mogą być
inne wskaźniki omówione w tym rozdziale: oscylator stochastyczny (%K i %D), wskaźnik Williamsa
%R, CCI (Commodity Channel Index) lub wskaźnik zmian ROC (Rate of Change). Można też
zastosować filtr kierunku zmian ceny, pasma Bollingera lub warunek utrzymania sygnału przez
kilka próbek. Zastosowany wskaźnik i regułę jego użycia należy dokładnie opisać w prezentacji.
• Modyfikacja MACD. Można zmienić parametry (12, 26, 9) i przeanalizować, dla jakich parametrów
oraz transakcji działanie algorytmu się zmienia.
• Przesunięcie sygnałów w czasie. Można zbadać wpływ późniejszego wykonania transakcji na
wynik oraz opóźnienie reakcji MACD. Przesunięcie sygnału wstecz korzysta z przyszłych informacji,
więc służy wyłącznie diagnozie opóźnienia, nie symulacji wykonalnej strategii.
Dodatkowo, rezultaty analizy można porównać z rezultatami zastosowania strategii „kup i trzymaj”:
realizowany jest zakup za cały kapitał w próbce 100 i utrzymanie instrumentu do końca danych.
Przy badaniu cech zmodyfikowanego algorytmu należy odnieść się do rezultatów otrzymanych dla
opisanego w p. 5.2 zestawu danych przy zastosowaniu algorytmu podstawowego. Należy ocenić, czy
modyfikacja poprawia stopę zwrotu lub inne jasno zdefiniowane miary względem algorytmu podstawowego (np. ogranicza maksymalną stratę). Brak poprawy stopy zwrotu lub innych badanych miar
jakości działania algorytmu nie wyklucza uzyskania pełnej punktacji za poprawnie przeprowadzoną
analizę i prezentację rezultatów. Porównanie rezultatów i analiza porównawcza działania obu
algorytmów pełni w tej części projektu bardzo istotną rolę.
7
5.2 Wspólny zbiór: analiza globalna i lokalna
Do analizy cech eksperymentalnych algorytmów należy stosować rezultaty ich działania, gdy dane
wejściowe stanowią wszystkie notowania udostępnione w pliku dane_pro1.zip na portalu eNauczanie.
Plik ten zawiera ponad 100 wektorów cen różnych spółek obejmujących sesje od 4 stycznia 2021 r.
do 31 grudnia 2024 r. Spółki wybrano spośród tych, które w tym okresie należały do indeksu Nasdaq-100
co najmniej podczas jednej sesji. Uwzględniono tylko spółki, dla których uzyskano kompletne notowania
z całego okresu. Każdy plik CSV zawiera 1005 obserwacji dla tych samych dat sesji oraz kolumny
date, open, high, low, close, volume. Ceny są wyrażone w USD. Do obliczeń MACD należy
użyć kolumny close, a do wykresu świecowego czterech kolumn cenowych OHLC.
Dla każdego wektora cen należy osobno uruchomić podstawowy algorytm MACD oraz badany zmodyfikowany algorytm, z tą samą regułą kapitału początkowego, która może się różnić od C100 = 1000x100,
z uwzględnianiem sygnałów od próbki 101 i opisaniem wybranego opóźnienia d. Zbiorczą ocenę skuteczności badanych algorytmów można ocenić np. na podstawie uśrednionej stopy zwrotu wyznaczonej
dla wszystkich wektorów cen.
W prezentacji należy przedstawić:
• Wynik globalny. Porównanie stopy zwrotu dla wszystkich wektorów cen lub innego parametru
opisującego całą symulację. Można przedstawić średnią i medianę zmiany wyniku oraz liczbę
instrumentów, dla których modyfikacja pomogła, zaszkodziła lub nie zmieniła rezultatu.
• Przykład lokalny. Wykres fragmentu danych pokazujący zmianę decyzji i wyniku transakcji,
z kryterium wyboru przykładu i odniesieniem do całego zbioru. Warto przedstawić także przypadek
pogorszenia stopy zwrotu zamkniętej transakcji, jeśli wystąpił.
Uwagi dodatkowe:
• Różnicę stóp zwrotu wyraża się w punktach procentowych.
• Nie należy sumować kapitałów wyrażonych w różnych jednostkach.
6 Prezentacje, punktacja i oddawane pliki
6.1 Dwie prezentacje
Obowiązują zasady zaliczenia projektu, które określają, że do każdego projektu należy przygotować:
• Prezentację wstępną, która obejmuje slajd tytułowy, krótki opis badanego algorytmu (punkt 4)
oraz opis współpracy z AI: konfigurację, wybrane prompty i ich rezultaty i ocenę.
• Prezentację końcową, która oprócz tego, że zawiera slajd tytułowy, wstęp i opis współpracy z AI,
to w głównej swojej części prezentuje osiągnięte rezultaty numeryczne oraz ich analizę w powiązaniu
z wykazaniem cech badanego algorytmu.
Obie prezentacje powinny zawierać:
• krótki wstęp zawierający opis badanego algorytmu,
• raport o błędach AI (około trzech slajdów) lub deklarację niewykrycia błędów AI o brzmieniu
podanym w zasadach zaliczenia projektu,
• recenzję AI: opis recenzenta i kryteriów jego budowy, prompt zaczynający recenzję lub jego fragmenty,
ocenę słowną i liczbową 1–10. Zaleca się około czterech slajdów recenzji, najlepiej jeden z oceną.
Nie każdy slajd prezentacji trzeba dokładnie omawiać, można skoncentrować swoją wypowiedź
na najciekawszych rezultatach, przy czym elementy obowiązkowe zawsze należy krótko omówić.
6.2 Punktacja
Maksymalną punktację za prezentację wstępną określa tabela 1, natomiast za prezentację końcową
tabela 2. Oceniana będzie jakość analizy badanego algorytmu oraz zgodność z wymaganiami a nie
wysokość zysku ani liczba użytych narzędzi AI.
8
Tabela 1: Prezentacja wstępna: maksymalna punktacja
Oceniany element Punkty
Wstęp (opis algorytmu MACD). 0,4
Sposób pracy i istotne elementy konfiguracji narzędzi AI. 0,4
Wybrany prompt, rezultat i jego ocena. 0,4
Raport o błędach AI lub deklaracja ich niewykrycia. 0,4
Recenzent, prompt recenzji oraz końcowa ocena słowna i liczbowa. 0,4
Razem 2
Tabela 2: Prezentacja końcowa: maksymalna punktacja
Oceniany element Punkty
Wstęp i opis współpracy z AI według kryteriów z tabeli 1. 2,0
Czytelna interpretacja wykresów A1, B1, C1 i C2. 1,5
Analiza wybranej transakcji, wykres D1. 0,5
Symulacja całego szeregu, wykresy E1 i E2, statystyki i wnioski ze slajdu F. 2,0
Część eksperymentalna: uzasadnienie i opis zmodyfikowanego algorytmu (0,5), analiza
zbioru wektorów cen (1,0), interpretacja przykładu lokalnego (0,5).
2,0
Razem 8
Za część podstawową projektu 1 można otrzymać maksymalnie 8 punktów. Jeśli część eksperymentalna
projektu 1 zawierać będzie tylko porównanie z metodą inwestowania „kup i trzymaj”, to ta część pracy
zostanie oceniona na maksymalnie 0,5 punktu.
6.3 Program i archiwa
Kod należy przygotować w plikach .py, bez plików Jupyter Notebook. Skrypty i katalogi można
zorganizować dowolnie. Kod obu części projektu musi odtwarzać wyniki prezentowane na slajdach.
Na eNauczanie należy przesłać (opis symboli zawarty jest w zasadach zaliczenia projektu):
• w terminie P2 jeden ZIP ze slajdami prezentacji wstępnej w formacie PDF, źródłami LaTeX,
Makefile i plikami potrzebnymi do kompilacji,
• w terminie P3 ZIP nr 1 ze slajdami prezentacji końcowej obejmującej obie realizowane części
projektu, źródłami LaTeX, Makefile i plikami potrzebnymi do kompilacji,
• w terminie P3 ZIP nr 2 ze wszystkimi kodami części podstawowej i eksperymentalnej, danymi wejściowymi wymaganymi do uruchomienia kodu z części podstawowej oraz plikiem readme.md.
Jeżeli wykorzystano szablony lub materiały pomocnicze, do ZIP-u z kodem należy dołączyć plik
zrodla.md ze wskazaniem ich źródeł. Plik ten należy umieścić w głównym katalogu zawierającym kody
źródłowe programu.
Ze względu na rozmiar wspólnego zbioru nie należy dołączać danych części eksperymentalnej
do przesyłanego archiwum. Kod może odczytywać te dane z lokalnego katalogu projektu, który nie
jest dołączany do ZIP-u, albo korzystać ze zmiennej wskazującej katalog z danymi w innej lokalizacji.
W pliku readme.md należy wyjaśnić funkcjonalność kodu i sposób uruchamiania obliczeń, opisać, gdzie
umieścić dane eksperymentalne lub jak ustawić ścieżkę do ich katalogu, wymienić wymagane pakiety
i podać polecenia generujące każdy wykres, używając dla części podstawowej oznaczeń z punktu 4.2,
np. „wykresy A1, B1, C1, C2, D1, E1 i E2: python wykresy.py”. Jedno polecenie może generować
wszystkie wykresy. Nie należy dołączać .venv ani plików konfigurujących narzędzia AI.
Każda osoba przesyła materiały na oba terminy, najpóźniej godzinę przed zajęciami określonymi
w harmonogramie zajęć, i wygłasza jedną prezentację. Kod musi być przesłany i poprawny, aby
utrzymać ocenę z prezentacji.
9
Źródła
[1] John J. Murphy, Analiza techniczna rynków finansowych, Maklerska.pl, 2017,
[2] Fidelity, Wprowadzenie do analizy technicznej,
[3] Fidelity, MACD – Technical Indicator Guide,
[4] pandas, Series.ewm,
[5] TradingView, Repainting: historical vs realtime calculations,
[6] Nasdaq, The Nasdaq Opening and Closing Crosses,
[7] Fidelity, Exponential Moving Average,
[8] Backtrader, Orders – Creation/Execution,
[9] Python, PEP 8 – Function and Variable Names,
[10] QuantConnect, Portfolio – Key Concepts,
[11] TradingView, Introduction to candlestick charts and patterns.
