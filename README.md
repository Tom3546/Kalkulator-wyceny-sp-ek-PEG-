# Kalkulator-wyceny-spolek-PEG-

## Opis

Terminalowy kalkulator fundamentalny, który umożliwia szybkie sprawdzenie wyceny spółki na podstawie wskaźnika **PEG**.  
Program pobiera podstawowe dane finansowe spółki i ocenia jej atrakcyjność inwestycyjną.

## Działanie

* Program pobiera informacje o spółce za pomocą biblioteki yfinance.
Wyświetla podstawowe informacje finansowe:
  * **Name** - nazwa spółki
  * **Price** – bieżąca cena akcji
  * **P/E** – wskaźnik cena/zysk
  * **EPS growth** – roczny wzrost EPS
  * **PEG** – wskaźnik P/E w stosunku do wzrostu EPS
  * **Ocena** - Ocenia atrakcyjność spółki na podstawie wskaźnika PEG

Ocena spółki na podstawie PEG:
  * **Tania** – PEG ≤ 1
  * **Można inwestować** – PEG ≤ 2,5
  * **Watchlist** – PEG > 2,5

