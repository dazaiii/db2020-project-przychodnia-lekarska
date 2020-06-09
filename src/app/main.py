from typing import Optional, Any
import pymysql
import functions

print('Menu')
print('1. Zarejestruj pacjenta')
print('2. Wyswietl receptę')
print('3. Sprawdz czy lekarz jest na urlopie')
print('4. Wyświetl dane kontaktowe lekarza')
print('5. Wyświetl godziny przyjęć wszystkich lekarzy alfabetycznie')
print('6. Wyświetl wizyty danego lekarza w danym dniu')
print('7. Wyświetl zaplanowane wizyty w danym gabinecie')

opcja = int(input('Wybierz opcje: '))
print(opcja)


#Zarejestruj pacjenta
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


#Wyświetl receptę
elif opcja == 2:
    imie = input('Podaj imie pacjenta: ')
    nazwisko = input('Podaj nazwikso pacjenta: ')
    functions.recepta(imie, nazwisko)


#Wypisz lekarzy na urlopie i posegreguj ich alfabetycznie
elif opcja == 3:
    functions.na_urlopie()


#Wypisz dane kontaktowe lekarza podając jego imię i nazwisko
elif opcja == 4:
    imie_lekarza = input('Podaj imię lekarza: ')
    nazwisko_lekarza = input('Podaj nazywa lekarza: ')
    functions.dane_kontaktowe_lekarza(imie_lekarza, nazwisko_lekarza)


#Wyświetl godziny przyjęć lekarzy
elif opcja == 5:
    functions.godziny_przyjec()


#Wyświetl wizyty danego lekarza w danym dniu
elif opcja == 6:
    imie_lekarza = input('Podaj imię lekarza: ')
    nazwisko_lekarza = input('Podaj nazywa lekarza: ')
    dzien = input('Podaj dzień w formacie RRRR-MM-DD: ')
    functions.wizyty_lekarza_w_dniu(imie_lekarza, nazwisko_lekarza, dzien)


#Wyświetl zaplanowane wizyty w danym gabinecie
elif opcja == 7:
    nr_gabinetu = input('Podaj numer gabinetu: ')
    functions.wizyty_gabinet(nr_gabinetu)