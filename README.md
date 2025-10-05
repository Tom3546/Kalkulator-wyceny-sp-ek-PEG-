# Kalkulator-wyceny-spolek-PEG-

## Opis

Terminalowy kalkulator fundamentalny, który umożliwia szybkie sprawdzenie wyceny spółki na podstawie wskaźnika **PEG**.  
Program pobiera podstawowe dane finansowe spółki i ocenia jej atrakcyjność inwestycyjną.

## Działanie

Program pobiera informacje o spółce za pomocą biblioteki yfinance, a następnie wyświetla podstawowe informcaje finansowe:

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

## Instrukcja obsługi

1. Uruchom plik peg_calc.bat
2. Wpisz ticker spółki (możesz go znaleśc na stronie yahoo finance np: XTB S.A. (XTB.WA)). Dla Polskich spółek wpisywanie koncówki `.WA` nie jest konieczne, ponieważ program automatycznie sprawdzi czy taki ticker istnieje. 
**Uwaga:** Automatyczne dodanie `.WA` nie zawsze działa poprawnie — jeśli Yahoo Finance znajdzie ticker bez końcówki `.WA`, możesz otrzymać dane dotyczące innej spółki niż ta, którą chciałeś sprawdzić.  
Dlatego zawsze sprawdzaj, czy nazwa spółki wyświetlana przez program zgadza się z tą, którą chciałeś analizować.
