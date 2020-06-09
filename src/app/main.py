from typing import Optional, Any
import pymysql
import functions

print('Menu')
print('1. Zarejestruj pacjenta')
print('2. Wyswietl receptę')
print('3. Wypisz lekarzy na urlopie/nie na urlopie')
print('4. Wyświetl dane kontaktowe')
print('5. Wyświetl godziny przyjęć lekarzy')
print('6. Wyświetl godziny przyjęć i gabinet konkretnego lekarza')


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


#Wyświetl receptę danego pacjenta
elif opcja == 2:
    imie = input('Podaj imie pacjenta: ')
    nazwisko = input('Podaj nazwisko pacjenta: ')
    functions.recepta(imie, nazwisko)


#Wypisz lekarzy na urlopie/nie na urlopie
elif opcja == 3:
    print('1. Wypisz lekarzy na urlopie')
    print('2. Wypisz lekarzy nie na urlopie')
    wybor = int(input('Wybierz opcję 1 lub 2: '))

    if (wybor == 2):
        wybor = 0

    functions.na_urlopie(wybor)


#Wypisz dane kontaktowe
elif opcja == 4:

    print('Kogo dane kontaktowe chcesz wypisać?')
    print('1. Lekarza')
    print('2. Pacjenta')
    wybor = int(input('Wybierz opcję 1 lub 2: '))

    if(wybor == 1):
        print('Chcesz wypisać:')
        print('1. Dane kontaktowe wszystkich lekarzy')
        print('2. Dane kontaktowe konkretnego lekarza')
        wybor2 = int(input('Wybierz opcję 1 lub 2: '))

        if(wybor2 == 1):
            functions.dane_kontaktowe('pracownik')
        else:
            imie_lekarza = input('Podaj imię lekarza: ')
            nazwisko_lekarza = input('Podaj nazwisko lekarza: ')
            functions.dane_kontaktowe_1('pracownik', imie_lekarza, nazwisko_lekarza)

    elif(wybor == 2):
        print('Chcesz wypisać:')
        print('1. Dane kontaktowe wszystkich pacjentów')
        print('2. Dane kontaktowe konkretnego pacjenta')
        wybor2 = int(input('Wybierz opcję 1 lub 2: '))

        if (wybor2 == 1):
            functions.dane_kontaktowe('pacjent')
        else:
            imie_pacjenta = input('Podaj imię pacjenta: ')
            nazwisko_pacjenta = input('Podaj nazwisko pacjenta: ')
            functions.dane_kontaktowe_1('pacjent', imie_pacjenta, nazwisko_pacjenta)

#Wyświetl godziny przyjęć lekarzy
elif opcja == 5:
    print('Wyświetl godziny przyjęć:')
    print('1. Wszystkich lekarzy')
    print('2. Jednego lekarza')
    wybor = int(input('Wybierz opcję 1 lub 2: '))

    if (wybor == 1):
        functions.godziny_przyjec()

    else:
        imie_lekarza = input('Podaj imię lekarza: ')
        nazwisko_lekarza = input('Podaj nazwisko lekarza: ')
        functions.godziny_przyjec_lekarza(imie_lekarza, nazwisko_lekarza)