# Kalkulator wyceny spółek PEG
## Opis

Terminalowy kalkulator fundamentalny, który umożliwia szybkie sprawdzenie wyceny spółki na podstawie wskaźnika **PEG**.  
Program pobiera podstawowe dane finansowe spółki i ocenia jej atrakcyjność inwestycyjną.

## Działanie

Program korzysta z biblioteki **yfinance**, aby pobrać informacje o spółce i wyświetlić kluczowe wskaźniki finansowe:

- **Name** – nazwa spółki  
- **Price** – bieżąca cena akcji  
- **P/E** – wskaźnik cena/zysk  
- **EPS growth** – roczny wzrost EPS  
- **PEG** – wskaźnik P/E w stosunku do wzrostu EPS  
- **Ocena** – klasyfikacja spółki na podstawie wskaźnika PEG

Ocena spółki według PEG:

- **Tania** – PEG ≤ 1  
- **Można inwestować** – PEG ≤ 2,5  
- **Watchlist** – PEG > 2,5

## Instrukcja obsługi

1. Zainstaluj wymagane biblioteki Pythona, korzystając z pliku `requirements.txt`:
   * Pobierz pliki
   * W terminalu, w folderze projektu, uruchom:
  ```bash
pip install -r requirements.txt```

3. Uruchom plik `peg_calc.bat`.  
4. Wpisz ticker spółki (możesz go znaleźć na stronie Yahoo Finance, np. **XTB S.A. (XTB.WA)**).  
   - Dla polskich spółek wpisywanie końcówki `.WA` nie jest konieczne — program automatycznie sprawdzi, czy taki ticker istnieje.  
   - **Uwaga:** Automatyczne dodanie `.WA` nie zawsze działa poprawnie. Jeśli Yahoo Finance znajdzie ticker bez końcówki `.WA`, możesz otrzymać dane dotyczące innej spółki niż ta, którą chciałeś sprawdzić.  
   Dlatego zawsze sprawdzaj, czy nazwa spółki wyświetlana przez program zgadza się z tą, którą chciałeś analizować.
