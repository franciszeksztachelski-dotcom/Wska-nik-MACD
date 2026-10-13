Narzędzia do pracy z agentami AI 2 października 2026
Autorzy: Piotr Sypek, ChatGPT
1 Programowanie z wykorzystaniem agentów AI
W projektach z metod numerycznych korzystanie z AI jest wymagane, jednak wybór narzędzi AI jest dowolny.
Sugerowane jest wybranie takiego narzędzia AI, które umożliwia programowanie z wykorzystaniem agentów AI (ang.
agentic coding). Programowanie z wykorzystaniem agentów AI polega na powierzaniu agentowi zadania: analizuje on
projekt, edytuje pliki, wykonuje polecenia, sprawdza rezultaty i wprowadza poprawki pod nadzorem użytkownika.
2 Rekomendowane narzędzia
Na początek warto wybrać jedno narzędzie i opanować pracę z nim na całym projekcie: od obliczeń do gotowej
prezentacji. Poniższa lista przedstawia alternatywy dopasowane do różnych sposobów pracy. Szczegóły, licencje, adresy
stron i oceny wszystkich narzędzi znajdują się w punkcie 4.
• Codex – rekomendowany do prowadzenia całego projektu Python i LaTeX w jednym katalogu. Wariant desktopowy
ułatwia przegląd zmian, a CLI i rozszerzenie IDE pozwalają dobrać interfejs do własnego sposobu pracy.
• Claude Code – rekomendowany do wieloetapowej implementacji, diagnozowania błędów i recenzji. Przydatny, gdy
agent ma naprzemiennie czytać kod, wprowadzać zmiany i sprawdzać wyniki poleceń.
• Cline – otwarte oprogramowanie dla osób pracujących w VS Code. Rozdzielenie planowania i wykonania oraz
zatwierdzanie operacji sprzyjają nauce świadomego nadzorowania agenta.
• Cursor – edytor dla osób preferujących zintegrowane środowisko z agentem, terminalem i podglądem zmian.
Wygodny do równoległego rozwijania skryptów obliczeniowych i źródeł prezentacji.
• OpenCode – otwarte oprogramowanie z wyborem modeli i interfejsów. Warto je rozważyć, gdy istotna jest
elastyczność konfiguracji i praca na lokalnym projekcie.
• Aider – dobry wybór do kontrolowanych zmian w repozytorium Git. Pozwala powiązać edycję z testami i poleceniem
budowania projektu, co pomaga utrzymać odtwarzalność obliczeń i kompilacji.
• Pi – narzędzie dla osób chcących lepiej poznać i samodzielnie dostosować działanie agenta. Niewielki rdzeń i
rozszerzenia dają dużą swobodę, ale wymagają więcej pracy nad konfiguracją i kontrolą uprawnień.
3 Ranking narzędzi AI
W punkcie 4 jest przedstawiona lista narzędzi AI, która została przygotowana wraz z oceną narzędzi AI przy pomocy
Codex. Ocenę narzędzi w formie rankingu opracowano jako orientacyjną, autorską ocenę przydatności do całego
projektu Python + LaTeX + PDF. Podstawą są udokumentowane możliwości, sposób pracy i stan utrzymania
narzędzi. Nie przeprowadzono wspólnego testu wykonawczego wszystkich aplikacji, więc liczby nie są wynikami pomiaru
skuteczności. Ocena łączy pięć kryteriów, każde w skali 1–10:
• Python i repozytorium – 30%: analiza kontekstu, spójna edycja wielu plików, wykonywanie obliczeń i testów,
• LaTeX i PDF – 25%: praca nad źródłami, uruchamianie kompilacji, diagnoza błędów i możliwość kontroli
wizualnej rezultatu,
• Weryfikacja i odtwarzalność – 20%: poprawianie błędów na podstawie rzeczywistych wyników poleceń i
powtarzalność procesu,
• Kontrola pracy – 15%: przegląd i cofanie zmian, uprawnienia, historia oraz możliwość przekazania instrukcji
projektu,
• Gotowość do użycia – 10%: konfiguracja, dokumentacja, utrzymanie, koszty, limity i dostępność.
Średnią ważoną zaokrąglono do liczby całkowitej. Wartości 9–10 oznaczają bardzo dobre pokrycie całego procesu, 7–8 –
dobry wybór po konfiguracji, 5–6 – rozwiązanie wymagające więcej uzupełnień, 3–4 – ograniczone dopasowanie, a 1–2
– bardzo małą bieżącą przydatność. Dla projektów bez aktywnego rozwoju przyjęto limit 4, a dla wyłączonych usług
lub braku dostępu dla nowych użytkowników – 2. Niska ocena narzędzia specjalistycznego nie oznacza niskiej jakości
w jego właściwym zastosowaniu. Oceny mniejszych projektów są bardziej niepewne. Wynik zależy też od wybranego
modelu, konfiguracji, limitów i dostępu do Pythona, LaTeX-a oraz narzędzi do oglądania PDF-u.
Wyboru należy dokonać samodzielnie, na podstawie własnej oceny i prób z projektem. Wybór narzędzia
oraz jego ocena w tym rankingu nie mają żadnego wpływu na ocenę z projektu MN. Ocenie podlegają
oddane materiały i spełnienie warunków zaliczenia projektu. Ranking nie jest również oceną recenzenta AI, którą
należy przedstawić we własnej prezentacji.
1
4 Przegląd narzędzi AI
Pierwsza tabela łączy aplikacje, edytory i rozszerzenia IDE z asystentami ogólnego przeznaczenia oraz automatyzacją
komputera. Opisy rozróżniają ich zastosowania. Kolejne tabele obejmują narzędzia terminalowe, usługi chmurowe oraz
projekty wycofane lub z ograniczonym dostępem. W każdej tabeli obowiązuje kolejność malejąca według oceny, a przy
tej samej ocenie – alfabetyczna.
Zielone tło całego wiersza wyróżnia wyniki 9–10. Przegląd obejmuje także agentów ogólnego przeznaczenia, automatyzację pulpitu i koordynację innych agentów. MCP to sposób dołączania narzędzi, a ACP – łączenia aplikacji z
zewnętrznym agentem. W opisach wskazano istotne zależności od rozszerzeń i środowiska wykonawczego. Ocena takiej
aplikacji zakłada ich skonfigurowanie. Lista powstała na podstawie oficjalnej dokumentacji i repozytoriów, nie stanowi
pełnego katalogu rynku. Funkcje eksperymentalne i stan utrzymania mogą się zmieniać. Samo pobranie aplikacji nie
zapewnia środowiska Python i LaTeX ani możliwości oglądania PDF-u.
Tabela 1: Aplikacje, edytory i asystenci AI
Narzędzie / strona Zastosowanie i sposób pracy Kod / licencja Ocena
Cline
github.com/cline/cline
Agent z planowaniem, edycją plików i uruchamianiem
poleceń. Oprócz rozszerzenia ma CLI i aplikację
desktopową.
Otwarty
Apache-2.0
9
Codex / ChatGPT Desktop
openai.com/codex
Aplikacja OpenAI do pracy z projektami, plikami i
zadaniami agentowymi. Osobne warianty CLI i IDE
opisano dalej.
Zamknięty 9
Codex IDE extension
learn.chatgpt.com/docs/codex/ide
Rozszerzenie OpenAI. Agent korzysta z kontekstu
projektu, edytuje kod i pokazuje zmiany w edytorze.
Zamknięty 9
Cursor
cursor.com
Edytor firmy Anysphere z agentem analizującym i
zmieniającym projekt. Dostępny także osobny CLI.
Zamknięty 9
Augment / Auggie
docs.augmentcode.com/cli/overvie
w
Narzędzia Augment Code do pracy z dużą bazą kodu.
Rozszerzenie IDE i agent terminalowy Auggie.
Zamknięty 8
Claude Desktop / Cowork
claude.com/download
Aplikacja Anthropic. Cowork wykonuje zadania na
plikach, a integracja z Claude Code służy pracy nad
kodem.
Zamknięty 8
Devin Desktop (dawniej
Windsurf)
devin.ai/desktop
Aplikacja Cognition z edytorem i zarządzaniem agentami.
Łączy pracę nad kodem z delegowaniem zadań.
Zamknięty 8
GitHub Copilot
github.com/features/copilot
Narzędzia GitHub do pracy w edytorze, terminalu i
chmurze. Tryb agentowy wykonuje zadania w projekcie.
VS Code: MIT
usługi: kod zamknięty
8
Google Antigravity
antigravity.google
Środowisko Google do pracy z agentami. Łączy edytor,
terminal i przeglądarkę, ma również CLI.
Zamknięty 8
Goose
goose-docs.ai
Lokalny agent z aplikacją i CLI. Programowanie, analiza
danych i automatyzacja przez dołączane narzędzia.
Otwarty
Apache-2.0
8
JetBrains Junie
junie.jetbrains.com
Agent JetBrains realizujący zadania, uruchamiający
testy i wykorzystujący funkcje IDE. Także w CLI.
Zamknięty 8
Kilo Code
github.com/Kilo-Org/kilocode
Agent do implementacji, debugowania i przeglądu kodu.
Oferuje integrację z edytorem oraz CLI.
Otwarty
MIT
8
Kiro
kiro.dev
Środowisko AWS do realizacji zadań na podstawie
specyfikacji. Dostępne jako IDE oraz CLI.
Zamknięty 8
OpenHands
github.com/OpenHands/OpenHan
ds
Agenci programistyczni i panel Agent Canvas. Praca
lokalna, własny serwer lub zdalne środowisko
wykonawcze.
Otwarty
MIT
8
OpenWork
github.com/different-ai/openwork
Graficzne środowisko pracy na lokalnych plikach, oparte
na OpenCode. Udostępnia zadania i skille. Wykonanie
zależy od silnika OpenCode i modelu.
Rdzeń: MIT
EE: OpenWork EE
License
8
Superset
github.com/superset-sh/superset
Środowisko do nadzorowania wielu agentów, terminali i
zmian w oddzielnych kopiach roboczych Git. Wymaga
wybranych agentów i dostępu do modeli.
Dostępny kod
Elastic License 2.0
8
2
Tabela 1. Aplikacje, edytory i asystenci AI – ciąg dalszy
Narzędzie / strona Zastosowanie i sposób pracy Kod / licencja Ocena
Verdent
www.verdent.ai
Narzędzie Verdent do równoległych zadań
programistycznych. Aplikacja desktopowa i integracja z
IDE.
Zamknięty 8
Vibe Kanban
github.com/BloopAI/vibe-kanban
Tablica zadań i kontrola równoległej pracy w osobnych
kopiach roboczych Git. Kod wykonują podłączeni agenci,
np. Codex lub Claude Code.
Otwarty
Apache-2.0
8
Zed
zed.dev/ai
Edytor z panelem agentowym. Obsługuje własne
narzędzia AI i podłączanie zewnętrznych agentów.
Otwarty
GPL-3.0+
części: Apache-2.0
8
Agent Zero
github.com/agent0ai/agent-zero
Agent z panelem, terminalem i pulpitem w kontenerze.
Wykonuje kod oraz deleguje zadania. Dostęp do plików
gospodarza wymaga udostępnienia katalogu lub łącznika.
Otwarty
MIT
7
Amazon Q Developer
aws.amazon.com/q/developer
Asystent i agent AWS w IDE, szczególnie przydatny
przy usługach AWS. Wariant CLI ma osobny status.
VS Code: Apache-2.0
usługi: kod zamknięty
7
Avante.nvim
github.com/avante-corp/avante.nvi
m
Rozszerzenie Neovima z trybem agentowym, narzędziami
do kodu i obsługą ACP. Może korzystać z własnych
narzędzi albo podłączonego agenta.
Otwarty
Apache-2.0
7
CodeBuddy
www.codebuddy.ai/docs
Narzędzia Tencent: edytor, rozszerzenia i CLI. Agent
pomaga wdrażać zmiany w wielu plikach.
Zamknięty 7
CodeCompanion.nvim
github.com/olimorris/codecompani
on.nvim
Agent w Neovimie z edycją plików i wykonywaniem
poleceń. Obsługuje własne narzędzia oraz zewnętrznych
agentów przez ACP. Wymaga konfiguracji edytora.
Otwarty
Apache-2.0
7
Docker Agent (dawniej
cagent)
github.com/docker/docker-agent
Uruchamia agentów i zespoły opisane w YAML.
Narzędzia lokalne, MCP i dobór modeli. Użytkownik
przygotowuje konfigurację oraz środowisko wykonawcze.
Otwarty
Apache-2.0
7
Gemini Code Assist
docs.cloud.google.com/gemini/doc
s/codeassist/overview
Asystent Google w IDE. Wersje Standard i Enterprise
pozostają dostępne. Dostęp konsumencki przeniesiono do
Antigravity.
Zamknięty 7
Maestro (tinhtran24)
github.com/tinhtran24/maestro
Koordynuje zewnętrznych agentów, sesje, recenzje i
reakcje na błędy testów. Zapewnia osobne obszary pracy.
Mniejszy projekt wymagający konfiguracji.
Otwarty
Apache-2.0
7
OpenClaw
github.com/openclaw/openclaw
Dawniej Clawdbot i Moltbot. Asystent dostępny przez
komunikatory i panel, z pamięcią, plikami, poleceniami i
integracjami. Może też delegować kodowanie
podłączonym agentom.
Otwarty
MIT
7
Pochi
github.com/TabbyML/pochi
Agent w IDE do tworzenia aplikacji, wykonywania
poleceń i kontroli efektów pracy nad projektem.
Otwarty
Apache-2.0
7
Qoder
qoder.com
Platforma Qoder do pracy z agentami AI nad projektem,
z edytorem, planowaniem zadań i CLI.
Zamknięty 7
Refact.ai
github.com/JegernOUTT/refact
Agent do planowania, implementacji i testowania zmian.
Integracja z IDE i możliwość własnego wdrożenia.
Otwarty
BSD-3-Clause
7
TRAE
www.trae.ai
Środowisko ByteDance do tworzenia aplikacji z agentem.
Osobny projekt badawczy Trae Agent opisano dalej.
Zamknięty 7
ZCode
zcode.z.ai/en
Desktopowe środowisko Z.ai do pracy nad kodem z
wieloma agentami.
Zamknięty 7
Zencoder
zencoder.ai
Agenci Zencoder do implementacji, testów i utrzymania
kodu, dostępni z poziomu IDE.
Zamknięty 7
ZooCode
github.com/Zoo-Code-Org/Zoo-C
ode
Społecznościowa kontynuacja Roo Code. Agent w
edytorze do planowania, zmian w plikach i wykonywania
poleceń.
Otwarty
Apache-2.0
7
Agent TARS
agent-tars.com
Wielomodalny agent z CLI i panelem, łączący pliki,
terminal i przeglądarkę. Część możliwości pochodzi z
narzędzi MCP. Projekt rozwijany razem z UI-TARS
Desktop.
Otwarty
Apache-2.0
6
3
Tabela 1. Aplikacje, edytory i asystenci AI – ciąg dalszy
Narzędzie / strona Zastosowanie i sposób pracy Kod / licencja Ocena
AnythingLLM
github.com/Mintplex-Labs/anythi
ng-llm
Aplikacja desktopowa i panel do własnego wdrożenia.
Dokumenty, agenci, skille i MCP. Pełna praca nad
repozytorium wymaga odpowiednich narzędzi
wykonawczych.
Otwarty
MIT
6
AutoDev
github.com/phodal/auto-dev
Rozszerzalna platforma agentowa związana z IDE.
Automatyzuje zadania programistyczne i pracę z
narzędziami.
Otwarty
MPL-2.0
6
Baidu Comate
comate.baidu.com
Asystent Baidu do pracy z kodem w IDE, obejmujący
agenta programistycznego Zulu.
Zamknięty 6
Cherry Studio
github.com/CherryHQ/cherry-stu
dio
Aplikacja wielomodelowa z agentami i MCP. Zakres
działań na plikach oraz uruchamiania kodu zależy od
konfiguracji agenta i jego narzędzi.
Community:
AGPL-3.0
komercyjna: osobne
warunki
6
CodeGPT
www.codegpt.co
Asystenci i agenci CodeGPT zintegrowani z edytorem.
Praca nad kodem z kontekstem projektu.
Zamknięty 6
Hermes Agent
github.com/NousResearch/hermes
-agent
Asystent ogólnego przeznaczenia z terminalem, plikami,
pamięcią i umiejętnościami rozwijanymi na podstawie
wykonanych zadań. Obsługuje podagentów i
komunikatory. Python i LaTeX wymagają przygotowania
środowiska.
Otwarty
MIT
6
Jan Desktop
github.com/janhq/jan
Aplikacja do modeli lokalnych i chmurowych. Praca
agenta z plikami i powłoką wymaga dołączenia narzędzi
MCP. Osobny Jan Agent ma te funkcje wbudowane.
Otwarty
Apache-2.0
6
LibreChat
github.com/LibreChat-AI/LibreC
hat
Panel wielomodelowy z agentami, MCP i wykonywaniem
kodu. Dostęp do lokalnego projektu wymaga konfiguracji
środowiska. Dołączane obszary pracy są
eksperymentalne.
Otwarty
MIT
6
nanobot (HKUDS)
github.com/HKUDS/nanobot
Lekki asystent w Pythonie z narzędziami, pamięcią,
MCP i podagentami. Do pracy Python/LaTeX trzeba
przygotować środowisko oraz dostęp do projektu.
Otwarty
MIT
6
PicoClaw
github.com/sipeed/picoclaw
Asystent w Go inspirowany nanobotem, z narzędziami i
MCP. Przydatny do automatyzacji. Obliczenia i LaTeX
wymagają przygotowania środowiska.
Otwarty
MIT
6
Roomote
roomote.dev
Agent do własnego wdrożenia lub usługi hostowanej.
Analizuje repozytorium, wykonuje zadania i
przygotowuje zmiany.
Dostępny kod
FCL-1.0-ALv2
6
Sweep
github.com/sweepai/sweep
Obecnie asystent Sweep AI dla JetBrains. Publiczne
repozytorium wcześniejszego narzędzia ma odrębne
warunki użycia.
Wtyczka: zamknięta
repo: Sweep EE
6
Tabnine
www.tabnine.com
Asystent i agenci Tabnine dla zespołów. Integracja z IDE
oraz opcje prywatnego wdrożenia.
Zamknięty 6
Tongyi Lingma
lingma.aliyun.com
Asystent Alibaba w IDE z trybem samodzielnego
wykonywania zadań programistycznych.
Zamknięty 6
ZeroClaw
github.com/zeroclaw-labs/zeroclaw
Lokalny asystent w Rust z powłoką, przeglądarką i MCP.
Małe wymagania samego programu nie oznaczają
małych wymagań lokalnego modelu.
Otwarty
MIT lub Apache-2.0
6
Open WebUI
github.com/open-webui/open-web
ui
Panel dla modeli lokalnych i chmurowych z
wywoływaniem narzędzi. Edycję projektu i kompilację
trzeba zapewnić przez skonfigurowane narzędzia lub
integracje.
Dostępny kod
Open WebUI License
wymóg zachowania
marki
5
UI-TARS Desktop
github.com/bytedance/UI-TARS-d
esktop
Agent obsługujący interfejs graficzny na podstawie
obrazu ekranu. Wymaga zgodnego modelu wizyjnego.
Przydatny do obsługi aplikacji i kontroli dokumentów.
Otwarty
Apache-2.0
5
Unsloth Desktop / Studio
github.com/unslothai/unsloth
Interfejs do lokalnych modeli, czatu z narzędziami i
treningu. Studio to panel webowy, dostępna jest też
aplikacja.
UI: AGPL-3.0
rdzeń: Apache-2.0
5
4
Tabela 1. Aplikacje, edytory i asystenci AI – ciąg dalszy
Narzędzie / strona Zastosowanie i sposób pracy Kod / licencja Ocena
bolt.diy
github.com/stackblitz-labs/bolt.diy
Panel do samodzielnego uruchomienia i tworzenia
aplikacji webowych. Technologia WebContainers ma
osobne warunki.
Otwarty
MIT
4
CodeGeeX
codegeex.cn
Asystent Zhipu AI w IDE do generowania i wyjaśniania
kodu oraz testów. Narzędzie pomocnicze o mniejszej
autonomii.
Starszy kod:
Apache-2.0
usługi: osobne
warunki
4
Dyad
github.com/dyad-sh/dyad
Lokalna aplikacja do budowania aplikacji przez rozmowę.
Obejmuje otwarty rdzeń i funkcje Pro na innych
warunkach.
Rdzeń: Apache-2.0
Pro: FSL-1.1-ALv2
4
Tabby
github.com/TabbyML/tabby
Asystent do własnego wdrożenia: podpowiedzi kodu i
odpowiedzi o projekcie. Mniej autonomiczny niż typowy
agent.
Rdzeń: Apache-2.0
EE: osobna licencja
4
Browser Use WebUI
github.com/browser-use/web-ui
Gotowy panel do agenta przeglądarkowego. Wspiera
zbieranie danych i obsługę stron. Sam nie zapewnia
pełnego środowiska Python/LaTeX dla lokalnego
repozytorium.
Otwarty
MIT
3
Tabela 2: Agenci terminalowi i automatyzacja pracy z kodem
Narzędzie / strona Zastosowanie i sposób pracy Kod / licencja Ocena
Claude Code
code.claude.com/docs/en/overview
Agent Anthropic do wieloetapowej pracy nad projektem.
CLI oraz integracje z IDE i aplikacją desktopową.
Zamknięty 9
Codex CLI
github.com/openai/codex
Agent uruchamiany w katalogu projektu. Analizuje kod,
edytuje pliki, wykonuje polecenia i testy.
Otwarty
Apache-2.0
9
Aider
aider.chat
Programowanie w terminalu z integracją z Git. Zmiany
w wielu plikach, testy i sprawdzanie jakości kodu.
Otwarty
Apache-2.0
8
Amp
ampcode.com/docs
Agent Amp do terminala i edytora. Wykonuje
wieloetapowe zadania programistyczne z użyciem
narzędzi.
Zamknięty 8
Factory Droid
docs.factory.ai/droid-cli/quickstart
Agent Factory do pracy w terminalu i procesach zespołu.
Wykonuje zadania na repozytorium i sprawdza wyniki.
Zamknięty 8
Gemini CLI
github.com/google-gemini/gemini-c
li
Agent do plików, poleceń i narzędzi. Dostęp konsumencki
przez konto Google wycofano, pozostają m.in. klucze
API.
Otwarty
Apache-2.0
8
Kimi Code CLI
github.com/MoonshotAI/kimi-code
Agent terminalowy do edycji i testowania kodu. Obecna
wersja zastąpiła starszy, zarchiwizowany projekt kimi-cli.
Otwarty
MIT
starszy CLI:
Apache-2.0
8
Open Interpreter
github.com/openinterpreter/openi
nterpreter
Obecna wersja to agent terminalowy rozwinięty z Codex
CLI: edycja repozytorium, polecenia i przegląd zmian.
Nie należy utożsamiać jej ze starszym pakietem Python.
Otwarty
Apache-2.0
8
OpenCode
github.com/anomalyco/opencode
Agent do planowania i wykonywania zmian w projekcie.
Interfejs terminalowy oraz aplikacja desktopowa.
Otwarty
MIT
8
Warp
www.warp.dev
Terminal z agentami, podglądem zmian i przestrzenią
pracy nad projektem. Usługi chmurowe mają osobne
warunki.
Otwarty
AGPL-3.0
części UI: MIT
8
Atlassian Rovo Dev
www.atlassian.com/software/rov
o-dev
Agent Atlassian do terminala i pracy zespołowej. Łączy
zmiany w kodzie z kontekstem narzędzi zespołu.
Zamknięty 7
Code Assistant
github.com/stippi/code-assistant
Agent napisany w Rust, dostępny przez terminal,
aplikację graficzną i integrację z edytorem.
Otwarty
MIT
7
5
Tabela 2. Agenci terminalowi i automatyzacja pracy z kodem – ciąg dalszy
Narzędzie / strona Zastosowanie i sposób pracy Kod / licencja Ocena
Codebuff / Freebuff
github.com/Codebuf fAI/freebuff
Rodzina narzędzi z wyspecjalizowanymi agentami.
Obecne repozytorium Freebuff obejmuje terminal i inne
interfejsy.
Otwarty
Apache-2.0
7
Cosine
cosine.sh
Agenci Cosine do zadań programistycznych, dostępni
przez terminal i chmurę. Opcje wdrożeń dla organizacji.
Zamknięty 7
Crush
github.com/charmbracelet/crush
Agent z rozbudowanym interfejsem terminalowym. Praca
nad kodem i podłączanie narzędzi do projektu.
Dostępny kod
FSL-1.1-MIT
7
Deep Agents Code
docs.langchain.com/oss/deepagent
s/code/overview
Agent terminalowy oparty na Deep Agents. Planowanie
zadań, narzędzia, podagenci i trwała pamięć.
Otwarty
MIT
7
Every Code
github.com/just-every/code
Społecznościowe rozwinięcie Codex CLI, z dodatkowymi
automatyzacjami i pracą wielu agentów.
Otwarty
Apache-2.0
7
ForgeCode
github.com/tailcallhq/forgecode
Agent terminalowy do zmian w projekcie. Wcześniej
rozwijany jako Forge w organizacji Antinomy.
Otwarty
Apache-2.0
7
gptme
github.com/gptme/gptme
Asystent terminalowy, który edytuje kod i wykonuje
polecenia. Przydatny także do skryptów i pracy z
danymi.
Otwarty
MIT
7
Grok Build
github.com/xai-org/grok-build
Środowisko agenta programistycznego z interfejsem
terminalowym i możliwością integracji z edytorem.
Otwarty
Apache-2.0
7
Jan Agent
www.jan.ai/docs/agent
Terminalowy agent projektu Jan. Wbudowany odczyt i
zapis plików, polecenia i MCP. Korzysta ze wspólnej
konfiguracji z Jan Desktop. Wersja preview.
Otwarty
Apache-2.0
7
Letta Code
github.com/letta-ai/letta-code
Agent programistyczny z trwałą pamięcią, zachowujący
kontekst między kolejnymi sesjami pracy.
Otwarty
Apache-2.0
7
MiMo Code
github.com/XiaomiMiMo/MiMo-C
ode
Agent Xiaomi do zadań programistycznych.
Repozytorium zawiera dodatkowe ograniczenia
zastosowań.
Dostępny kod
MIT + zasady użycia
7
Mistral Vibe
github.com/mistralai/mistral-vibe
Agent terminalowy z dostępem do plików projektu i
powłoki. Wspiera iteracyjne zmiany i sprawdzanie ich
efektów.
Otwarty
Apache-2.0
7
Muse Code
dev.meta.ai/docs/muse-code
Agent Meta do terminala i automatycznych procesów.
Planuje, edytuje i uruchamia polecenia, korzystając z
podagentów.
Zamknięty 7
Nanocoder
github.com/Nano-Collective/nano
coder
Agent terminalowy do pracy z wybranym modelem, w
tym lokalnym. Projekt rozwijany przez społeczność.
Otwarty
MIT
7
Neovate Code
github.com/neovateai/neovate-code
Agent do interaktywnej pracy nad kodem i uruchamiania
zadań bez interfejsu użytkownika.
Otwarty
MIT
7
Oh My Pi
github.com/can1357/oh-my-pi
Rozwinięcie Pi z dodatkowymi narzędziami do
programowania i organizacji pracy agenta.
Otwarty
MIT
7
Pi
pi.dev
Niewielki, rozszerzalny agent terminalowy. Pozwala
samodzielnie dobierać modele, narzędzia i sposób pracy.
Otwarty
MIT
7
Plandex
github.com/plandex-ai/plandex
Agent do dużych zadań i planowania zmian w wielu
plikach. Można uruchomić własny serwer.
Otwarty
MIT
7
pool
github.com/poolsideai/pool
Agent Poolside do terminala i zgodnych edytorów.
Publiczne repozytorium nie oznacza otwartej licencji
aplikacji.
Zamknięty
Poolside EULA
7
Prime Agent
github.com/PrimeIntellect-ai/prim
e-agent
Agent wywodzący się z Pi. Łączy zadania
programistyczne i badawcze z delegowaniem pracy
podagentom.
Otwarty
MIT
7
Qwen Code
github.com/QwenLM/qwen-code
Agent terminalowy do rozumienia repozytorium,
wprowadzania zmian i uruchamiania narzędzi.
Otwarty
Apache-2.0
7
VT Code
github.com/vinhnx/VTCode
Agent terminalowy napisany w Rust do programowania i
wykonywania narzędzi w projekcie.
Otwarty
MIT lub Apache-2.0
7
6
Tabela 2. Agenci terminalowi i automatyzacja pracy z kodem – ciąg dalszy
Narzędzie / strona Zastosowanie i sposób pracy Kod / licencja Ocena
Zero (Gitlawb)
github.com/Gitlawb/zero
Niezależny agent terminalowy: pliki, polecenia, sesje i
uprawnienia. Obsługuje różne modele, także lokalne.
Mniejszy projekt wymagający własnych prób.
Otwarty
MIT
7
Blackbox AI CLI
docs.blackbox.ai/features/blackbox
-cli/introduction
Agent terminalowy platformy Blackbox AI do analizy
kodu i wykonywania zadań programistycznych.
Zamknięty 6
CodeWhale
github.com/Hmbown/Codewhale
Agent terminalowy w Rust do odczytu i edycji plików,
wykonywania poleceń oraz testów.
Otwarty
MIT
6
crow-cli
crow-ai.dev
Agent z pamięcią między sesjami. Działa w terminalu i
edytorach obsługujących protokół komunikacji z
agentem.
Otwarty
MIT
6
Dexto
github.com/truffle-ai/dexto
Konfigurowalne środowisko uruchamiania agentów,
obejmujące CLI do pracy nad kodem.
Dostępny kod
Elastic License 2.0
6
jcode
github.com/1jehuang/jcode
Lekki agent programistyczny napisany w Rust.
Terminalowy interfejs do pracy nad lokalnym projektem.
Otwarty
MIT
6
Kode CLI
github.com/shareAI-lab/Kode-CLI
Agent terminalowy do analizy projektu i wprowadzania
zmian z użyciem narzędzi programistycznych.
Otwarty
Apache-2.0
6
Minion Code
github.com/femto/minion-code
Agent inspirowany Claude Code. Licencja według pliku
LICENSE, mimo odmiennej deklaracji w README.
Otwarty
AGPL-3.0
6
RA.Aid
github.com/ai-christianson/RA.Aid
Agent do samodzielnego wykonywania wieloetapowych
zadań programistycznych z użyciem narzędzi.
Otwarty
Apache-2.0
6
siGit Code
github.com/getsigit/sigit
Agent nastawiony na pracę z lokalnymi modelami, z
opcjonalnym korzystaniem z usług chmurowych.
Otwarty
Apache-2.0
6
smith / Construct
github.com/construct-worlds/cons
truct
Agent smith w terminalowym środowisku Construct.
Łączy pracę nad projektem z narzędziami
deweloperskimi.
Otwarty
MIT
6
Tau
github.com/huggingface/tau
Minimalistyczny agent napisany w Pythonie, wywodzący
się z Pi. Dobry punkt odniesienia do analizy budowy
agenta.
Otwarty
MIT
6
g3
github.com/dhanji/g3
Eksperymentalny agent programistyczny wywodzący się
z Goose. Narzędzie do prób z automatyzacją pracy nad
kodem.
Otwarty
MIT
5
mini-SWE-agent
github.com/SWE-agent/mini-swe-a
gent
Niewielki agent do zadań na repozytorium. Przydatny w
badaniach oraz do poznania pętli działania agenta.
Otwarty
MIT
5
Raxol Coding Agent
github.com/DROOdotFOO/raxol
Agent w ekosystemie Elixir. Terminalowa praca nad
kodem z zatwierdzaniem edycji i poleceń.
Otwarty
MIT
5
Reasonix
github.com/esengine/DeepSeek-R
easonix
Agent terminalowy do pracy nad kodem, rozwijany z
myślą o modelach DeepSeek.
Otwarty
MIT
5
Stakpak
github.com/stakpak/agent
Agent do infrastruktury, wdrożeń i DevOps. Pomaga
konfigurować oraz diagnozować środowiska.
Otwarty
Apache-2.0
5
Trae Agent
github.com/bytedance/trae-agent
Otwarty agent badawczy do inżynierii oprogramowania.
Osobny projekt względem zamkniętego środowiska
TRAE.
Otwarty
MIT
5
Agentless
github.com/OpenAutoCoder/Agent
less
Badawczy proces automatycznej lokalizacji i naprawy
błędów. Nie jest ogólnym agentem konwersacyjnym.
Otwarty
MIT
4
AutoCodeRover
github.com/AutoCodeRoverSG/aut
o-code-rover
Narzędzie badawcze do rozwiązywania zgłoszeń i
naprawiania błędów z uwzględnieniem struktury
projektu.
Dostępny kod
Sonar
Source-Available v1.0
4
Devon
github.com/entropy-research/Devo
n
Eksperymentalny agent do pracy nad repozytorium, ze
szczególnym naciskiem na projekty w Pythonie.
Otwarty
AGPL-3.0
4
7
Tabela 3: Usługi chmurowe dostępne z własnego komputera
Narzędzie / strona Zastosowanie i sposób pracy Kod / licencja Ocena
Devin
devin.ai
Agent Cognition wykonujący zadania programistyczne w
zdalnym środowisku. Praca przez usługę, bez lokalnego
serwera.
Zamknięty 7
Ona
ona.com/cases/ona-agents
Usługa Ona do delegowania zadań agentom w zdalnych
środowiskach programistycznych i współpracy z nimi.
Zamknięty 7
GitLab Duo Agent Platform
docs.gitlab.com/user/duo_agent_p
latform
Agenci GitLab związani z repozytoriami i procesem
wytwarzania oprogramowania. Także wdrożenia
zarządzane przez organizację.
Mieszany
funkcje Duo: warunki
GitLab EE
6
Google Jules
jules.google
Agent Google do asynchronicznych zadań na
repozytorium. Przygotowuje zmiany w środowisku
chmurowym.
Zamknięty 6
Replit Agent
docs.replit.com/features/agent/ove
rview
Agent Replit tworzący i wdrażający aplikacje w
chmurowym środowisku. Obsługa przez przeglądarkę.
Zamknięty 5
Bolt
bolt.new
Usługa StackBlitz do tworzenia stron i aplikacji
webowych przez rozmowę. Środowisko pracy w
przeglądarce.
Zamknięty 3
Lovable
lovable.dev
Usługa Lovable do tworzenia aplikacji na podstawie
opisu, z podglądem i dalszym rozwijaniem projektu.
Zamknięty 3
v0
v0.app
Usługa Vercel do tworzenia interfejsów oraz aplikacji
webowych na podstawie rozmowy i materiałów
wejściowych.
Zamknięty 3
Tabela 4: Projekty wycofane, zastąpione lub z ograniczonym dostępem
Narzędzie / strona Zastosowanie i sposób pracy Kod / licencja Ocena
Amazon Q Developer CLI
github.com/aws/amazon-q-develop
er-cli
Starszy agent terminalowy, zastąpiony przez Kiro CLI.
Utrzymanie ograniczone do krytycznych poprawek
bezpieczeństwa.
Otwarty
MIT / Apache-2.0
4
Continue
github.com/continuedev/continue
Asystent IDE i CLI. Projekt nie jest już aktywnie
rozwijany, repozytorium pozostaje tylko do odczytu.
Otwarty
Apache-2.0
4
Roo Code
github.com/RooCodeInc/Roo-Code
Projekt zamknięty 15.05.2026. Kod pozostał dostępny, a
rozwój społecznościowy kontynuuje m.in. ZooCode.
Otwarty
Apache-2.0
4
SWE-agent
github.com/SWE-agent/SWE-age
nt
Badawczy agent do rozwiązywania zadań na
repozytorium. Twórcy wskazują mini-SWE-agent jako
następcę.
Otwarty
MIT
4
Firebase Studio
firebase.google.com/docs/studio
Środowisko Google w chmurze. Dostęp ograniczony do
istniejących przestrzeni roboczych, bez tworzenia
nowych.
Zamknięty 2
iFlow CLI
github.com/iflow-ai/iflow-cli
Usługę wyłączono 17.04.2026. Repozytorium pozostaje
materiałem archiwalnym i informacyjnym.
Brak potwierdzonej
licencji kodu