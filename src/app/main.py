from typing import Optional, Any
import pymysql
import functions

print('Menu')
opcja = int(input('Wybierz opcje: '))
print(opcja)

if opcja == 1:
    imie = input('Podaj imię: ')
    nazwisko = input('Podaj nazwisko: ')
    czy_ma_ubezpieczenie = functions.ubezpieczenie(imie, nazwisko)
    print(czy_ma_ubezpieczenie)
    if czy_ma_ubezpieczenie[0] == 1:
        print('Pacjent ma ubezpieczenie można go zarejestrować podaj dane lekarza.')
        imie_lekarza = input('Podaj imię lekarza: ')
        nazwisko_lekarza = input('Podaj nazwisko lekarza: ')
        czy_na_urlopie = functions.urlop(imie_lekarza, nazwisko_lekarza)
        if czy_na_urlopie[0] == 0:
            print('Można zarejestrować pacjenta podaj datę')
            godzina = str(input('Podaj godzinę w formaci (HH:MM:SS): '))
            data = str(input('Podaj datę w formacie (YYYY-MM-DD): '))
            dostepnosc_gabinetu = functions.dostepnosc_gabinetu(int(czy_na_urlopie[1]), godzina, data)
            if dostepnosc_gabinetu == 0:
                print('Można zarejestrować pacjenta na podaną godzinę')
                typ = input('Podaj typ wizyty: ')
                functions.zarejestruj(typ, str(czy_na_urlopie[1]), str(czy_ma_ubezpieczenie[1]), str(czy_na_urlopie[2]),
                                      data, godzina)
            else:
                print('Niestety gabinet jest zajęty.')
        else:
            print('Niestety wybrany lekarz znajduje się na urlopie.')
    else:
        print('Pacjent nie ma ubezpieczenia i nie może zostać zarejestrowany.')
