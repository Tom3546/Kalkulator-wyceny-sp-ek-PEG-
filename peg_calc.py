import yfinance as yf
from urllib.error import HTTPError
from colorama import Fore, Style
import os
import logging

logging.getLogger("yfinance").setLevel(logging.CRITICAL) #usuń do debugowania

def peg_calculator():
    ticker = input("Podaj ticker spółki: ").upper()

    os.system('cls' if os.name == 'nt' else 'clear')

    stock = yf.Ticker(ticker)

    def ticker_is_valid(ticker, stock):
        try:
            valid = bool("Basic EPS" in stock.financials.index and "regularMarketPrice" in stock.info)
            if valid == False:
                ticker = ticker + ".WA"
                stock = yf.Ticker(ticker)
                valid = bool("Basic EPS" in stock.financials.index)
                if valid == False:
                    return False
                if valid == True:
                    return ticker
            elif valid == True:
                return True
        except (HTTPError, KeyError, ValueError):
            return False
        except Exception:
            return False
        
    valid_ticker = ticker_is_valid(ticker, stock)

    if valid_ticker == False:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.RED}Wpisz poprawny ticker{Style.RESET_ALL}")
        return    
    elif valid_ticker != True:
        ticker = valid_ticker
        stock = yf.Ticker(ticker)

    name = stock.info["longName"]
    eps = stock.financials.loc["Basic EPS"] 
    n = len(eps) #liczymy od bierzącego roku kalendarzowego a nie od ttm

    price = stock.info["regularMarketPrice"]
    eps_prev = -1
    eps_prev_date = ""
    eps_curr = eps.iloc[0] # sprawdz czy społka ma eps > 0 , jeżeli n = 1  to wyswietl komiunikat "brak danych o eps z poprzednich lat"

    if eps_curr <= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.RED}Spółka jest stratna w tym roku{Style.RESET_ALL}")
        return
    
    pe = round(float(stock.info["trailingPE"]),2)

    for i in range(len(eps)-1, -1, -1):
        if eps.iloc[i] > 0:
            eps_prev = eps.iloc[i]
            eps_prev_date = eps.index[i].year
            break
        else:
            n-=1

    if n == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.RED}Brak danych o EPS z poprzednich lat{Style.RESET_ALL}")
        return

    eps_cagr = round(((eps_curr / eps_prev)**(1/n)-1)*100,2) #podaj cagr w n-latach

    if eps_cagr <= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.RED}Społka traci wartość eps{Style.RESET_ALL}")
        return

    peg = round(pe/eps_cagr,2)

    def ocena_peg(peg):
        if peg <=1:
            return f"{Fore.GREEN}TANIO{Style.RESET_ALL}"
        elif peg <=2.5:
            return f"{Fore.YELLOW}MOŻNA INWESTOWAĆ{Style.RESET_ALL}"
        else:
            return f"{Fore.RED}WATCHLIST{Style.RESET_ALL}"
        
    ocena = ocena_peg(peg)

    print(" Name:", name, "\n", "Price:", price, "\n", "P/E:", pe, "\n", "EPS growth past", n, "Y:", eps_cagr, "%", 
          "\n", "PEG:", peg, "\n", "Ocena: ", ocena)

peg_calculator()