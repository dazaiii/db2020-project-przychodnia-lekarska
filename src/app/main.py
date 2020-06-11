from typing import Optional, Any
import pymysql
import functions

print('Menu')
print('1. Zarejestruj pacjenta')
print('2. Wyswietl receptę')
print('3. Wypisz lekarzy na urlopie/nie na urlopie')
print('4. Wyświetl dane kontaktowe')
print('5. Wyświetl godziny przyjęć lekarzy')
print('6. Dodaj osobę do bazy')
print('7. Wyświetl wizyty')
print('8. Wyświetl historię wizyt pacjenta')
print('9. Wyświetl wszystkie skierowania danego pacjenta')
print('10. Modyfikuj dane kontaktowe')
print('11. Usuń wizytę z bazy')

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


#Dodaj osobę do bazy
elif opcja == 6:
    print('Kogo chcesz dodać?')
    print('1. Pacjenta')
    print('2. Pracownika')
    wybor = int(input('Wybierz opcję 1 lub 2: '))

    imie = input('Podaj imię: ')
    nazwisko = input('Podaj nazwisko: ')
    pesel = input('Podaj pesel: ')
    telefon = input('Podaj telefon: ')
    mail = input('Podaj mail: ')
    miejsce_zamieszkania = input('Podaj miejsce zamieszkania: ')
    data_urodzenia = input('Podaj datę urodzenia w formacie RRRR-MM-DD: ')

    if wybor == 1:
        id_pacjenta = functions.id_osoby('Pacjent')
        print(id_pacjenta)
        ubezpiecznie = str(input('Czy pacjent jest ubezpieczony? Tak/Nie: '))
        if ubezpiecznie == 'Tak':
            functions.dodaj_pacjenta(id_pacjenta,imie, nazwisko, data_urodzenia, pesel, miejsce_zamieszkania, telefon, mail,1)
        else:
            functions.dodaj_pacjenta(id_pacjenta,imie, nazwisko, data_urodzenia, pesel, miejsce_zamieszkania, telefon, mail,0)

    if wybor == 2:
        id_pracownika = functions.id_osoby('Pracownik')
        print('Kogo chcesz dodać: ')
        print('1. Lekarza')
        print('2. Pielęgniarkę')
        print('3. Recepcjonistkę')
        wybor2 = int(input('Wybierz opcję 1, 2 lub 3: '))
        if wybor2 == 1:
            functions.dodaj_pracownika(id_pracownika,imie,nazwisko,data_urodzenia,pesel,miejsce_zamieszkania,telefon,mail,'Lekarz')
            specjalizacja = input('Określ specjalizację lekarza: ')
            etat = input('Na jaki etat przyjąć lekarza: ')
            staz = input('Podaj staż pracy lekarza: ')
            functions.dodaj_lekarza(id_pracownika,specjalizacja,staz,etat)
        elif wybor2 == 2:
            functions.dodaj_pracownika(id_pracownika, imie, nazwisko, data_urodzenia, pesel, miejsce_zamieszkania, telefon, mail, 'Pielęgniarka')
        else:
            functions.dodaj_pracownika(id_pracownika, imie, nazwisko, data_urodzenia, pesel, miejsce_zamieszkania, telefon, mail, 'Recepcjonistka')



#Wyświetl wizyty
elif opcja == 7:
    print('Wyświetl wizyty:')
    print('1. Wszystkie')
    print('2. W danym dniu danego lekarza')
    print('3. W danym gabinecie')
    wybor = int(input('Wybierz opcję 1 lub 2: '))
    if wybor == 1:
        functions.wyswietl_wizyty()
    elif wybor == 2:
        imie_lekarza = input('Podaj imię lekarza: ')
        nazwisko_lekarza = input('Podaj nazwisko lekarza: ')
        dzien = input('Podaj dzień w formacie RRRR-MM-DD: ')
        functions.wizyty_lekarza_w_dniu(imie_lekarza, nazwisko_lekarza, dzien)
    else:
        nr_gabinetu = input('Podaj numer gabinetu: ')
        functions.wizyty_gabinet(nr_gabinetu)


#Wyświetl historię wizyt pacjenta
elif opcja == 8:
    imie = input('Podaj imie pajcenta: ')
    nazwisko = input('Podaj nazwisko pacjenta: ')
    functions.historia_wizyt(imie, nazwisko)


#Wyświetl wszystkie skierowania danego pacjenta
elif opcja == 9:
    imie_pacjenta = input('Podaj imię pacjenta: ')
    nazwisko_pacjenta = input('Podaj nazwisko pacjenta: ')
    functions.wyszukaj_skierowania(imie_pacjenta, nazwisko_pacjenta)


#Modyfikuj dane kontaktowe
elif opcja == 10:
    print('Kogo dane chcesz zmodyfikować: ')
    print('1. Pracownika')
    print('2. Pacjenta')
    wybor = int(input('Wybierz opcję 1 lub 2: '))

    if wybor == 1:
        tabela = 'Pracownik'
    else:
        tabela = 'Pacjent'

    imie = input('Podaj imię osoby której dane chcesz modyfikować: ')
    nazwisko = input('Podaj nazwisko osoby której dane chcesz modyfikować: ')

    print('Ktore dane chcesz modyfikować: ')
    print('1. Telefon')
    print('2. Mail')
    print('3. Miejsce zamieszkania')
    wybor2 = int(input('Wybierz opcję 1, 2 lub 3'))

    if wybor2 == 1:
        telefon = input('Podaj nowy numer telefonu: ')
        functions.modyfikuj_dane_kontaktowe(tabela,imie,nazwisko,'telefon',telefon)
    elif wybor2 == 2:
        mail = input('Podaj nowy mail: ')
        functions.modyfikuj_dane_kontaktowe(tabela, imie, nazwisko, 'mail', mail)
    else:
        miejsce = input('Podaj nowe miejsce zamieszkania: ')
        functions.modyfikuj_dane_kontaktowe(tabela, imie, nazwisko, 'miejsce_zamieszkania', miejsce)

elif opcja == 11:
    imie = input('Podaj imie pacjenta: ')
    nazwisko = input('Podaj nazwisko pacjenta: ')
    data = input('Podaj datę wizyty: ')
    godzina = input('Podaj godzinę wizyty: ')
    functions.odwolaj_wizyte(imie,nazwisko,data,godzina)