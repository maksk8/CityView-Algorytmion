@echo off
@chcp 1250
title Projekt Miejskie Widoki

:Menu
cls
echo 	Miejskie Widoki
echo		   Menu
echo.
echo 1) Uruchom program
echo 2) Stworzenie Backup'u
echo 3) Informacje o programie
echo 4) Wyjscie
echo.
set /p opcja=Wybierz: 
if %opcja%==1 goto Main
if %opcja%==2 goto Backup
if %opcja%==3 goto Info
if %opcja%==4 goto Exit
else call skrypt projekt.bat
:Main
cls
echo "Miejskie widoki"
echo.
call CityView.py
echo.
call raport.py
call raport.html
echo.
pause
goto Menu
:Backup
cls
set nazwa=Raport_%DATE:~0,2%_%DATE:~3,2%_%DATE:~-4%_%TIME:~0,2%_%TIME:~3,2%.html
copy raport.html backup\%nazwa%
echo.
pause
goto :MENU

:Info
echo Maksymilian Kolodynski
echo.
echo Zadanie 1 Algorytmion 2019/20 "Widoki Miejskie"
echo.
echo 	Program tworzy macierz 5x5, w ktorej kazda cyfra od 1 do 5 nie powtarza sie ani w wierszu ani w kolumnie
echo 	Nastepnie, dodaje tzw. obserwatorow z kazdej ze stron. 
echo 	Obserwator to liczb odpowiadajaca liczbie budynkow widocznych z danego miejsca.
echo 	Liczba w macierzy odpowiada ilosci pieter danego budynku, gdzie wyzszy budynek zaslania widok nizszego.

PAUSE
goto Menu
:Exit