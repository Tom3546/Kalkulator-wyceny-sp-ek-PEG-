@echo off
:START
cls
echo Uruchamianie kalkulatora PEG...
python "peg_calc.py"
echo.
echo Nacisnij ENTER, aby uruchomic ponownie lub wpisz EXIT, aby zakonczyc.
set /p choice= 
if /i "%choice%"=="EXIT" goto END
goto START

:END
echo Koniec programu.
pause
