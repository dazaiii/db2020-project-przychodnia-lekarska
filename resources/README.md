# Przychodnia lekarska

| Nazwisko i imię | Wydział | Kierunek | Semestr | Grupa | Rok akademicki |
| :-------------: | :-----: | :------: | :-----: | :---: | :------------: |
| Kinga Baryczka         | WIMiIP  | IS       |   4     | 1     | 2019/2020      |
| Karol Kawalec         | WIMiIP  | IS       |   4     | 1     | 2019/2020      |

## Projekt bazy danych
Tematem projektu było stworzenie bazy danych oraz aplikacji przychodni lekarskiej.
Baza danych składa się z 7 encji:
- Pacjent
- Recepta
- Wizyta
- Skierowanie
- Pracownik
- Lekarz
- Gabinet
  
Połączenie tabel odpowiednimi relacjami pozwoliło na łączenie różnych zapytań. Dzięki temu stworzono funkcjonalności przydatne w zarządzaniu przychodnią lekarską.
  
Schemat bazy danych:
  
![Przychodnia](https://github.com/dazaiii/db2020-project-przychodnia-lekarska/blob/master/resources/Przychodnia%20lekarska.svg)
  
Przykładowe zapytania tworzące:
  
Tworzenie tabel "Pacjent", "Pracownik", "Lekarz" i "Wizyta"
```sql
CREATE TABLE pacjent (
  ID_pacjenta int(10) NOT NULL,
  Imie varchar(50) NOT NULL,
  Nazwisko varchar(50) NOT NULL,
  Data_urodzenia date NOT NULL,
  Pesel varchar(11) NOT NULL,
  Miejsce_zamieszkania varchar(50) NOT NULL,
  Telefon int(10) NOT NULL,
  Mail varchar(50) NOT NULL,
  Ubezpieczenie int(1) NOT NULL
);

CREATE TABLE pracownik (
  ID_pracownika int(11) NOT NULL,
  Imie varchar(50) NOT NULL,
  Nazwisko varchar(50) NOT NULL,
  Data_urodzenia date NOT NULL,
  Pesel varchar(11) NOT NULL,
  Miejsce_zamieszkania varchar(50) NOT NULL,
  Telefon int(10) NOT NULL,
  Mail varchar(50) NOT NULL,
  Funkcja varchar(50) NOT NULL
);

CREATE TABLE lekarz (
  ID_pracownika int(10) NOT NULL,
  Specjalizacja varchar(50) NOT NULL,
  Staz_pracy int(10) NOT NULL,
  Etat varchar(50) NOT NULL,
  Urlop int(1) NOT NULL
);

CREATE TABLE wizyta (
  ID_wizyty int(10) NOT NULL,
  Typ varchar(50) NOT NULL,
  ID_pracownika int(10) NOT NULL,
  ID_pacjenta int(10) NOT NULL,
  ID_gabinetu int(10) NOT NULL,
  Data_wizyty date NOT NULL,
  Godzina_wizyty time NOT NULL
);
```
Dodanie relacji pomiędzy tabelami oraz kluczy głównych:
```sql
ALTER TABLE wizyta ADD CONSTRAINT wizyta_ibfk_1 FOREIGN KEY (ID_pacjenta) REFERENCES pacjent (ID_pacjenta);
  
ALTER TABLE wizyta ADD CONSTRAINT wizyta_ibfk_3 FOREIGN KEY (ID_pracownika) REFERENCES pracownik (ID_pracownika);

ALTER TABLE lekarz ADD CONSTRAINT lekarz_ibfk_1 FOREIGN KEY (ID_pracownika) REFERENCES pracownik (ID_pracownika);

ALTER TABLE pacjent ADD PRIMARY KEY (ID_pacjenta);

ALTER TABLE pracownik ADD PRIMARY KEY (ID_pracownika);

ALTER TABLE lekarz ADD PRIMARY KEY (ID_pracownika);

ALTER TABLE wizyta ADD PRIMARY KEY (ID_wizyty);
```

Wprowadzanie przykładowych danych do tabel:
```sql
INSERT INTO pracownik (ID_pracownika, Imie, Nazwisko, Data_urodzenia, Pesel, Miejsce_zamieszkania, Telefon, Mail, Funkcja)
VALUES(1, 'Piotr', 'Majewski', '1940-02-11', '40021167854', 'Kraków', 123456789, 'majewski@mail.com', 'Lekarz');

INSERT INTO pacjent (ID_pacjenta, Imie, Nazwisko, Data_urodzenia, Pesel, Miejsce_zamieszkania, Telefon, Mail, Ubezpieczenie)
VALUES(1, 'Adam', 'Nowak', '1920-02-11', '20021112345', 'Kraków', 123456789, 'an@mail.com', 1);

INSERT INTO lekarz (ID_pracownika, Specjalizacja, Staz_pracy, Etat, Urlop)
VALUES(1, 'Kardiolog', 1, 'staż', 0);

INSERT INTO wizyta (ID_wizyty, Typ, ID_pracownika, ID_pacjenta, ID_gabinetu, Data_wizyty, Godzina_wizyty)
VALUES(1, 'Badanie', 1, 2, 1, '2020-06-08', '10:00:00');
```

## Implementacja zapytań SQL

### Sekcja sprawdzania danych
   
1. Wyświetlenie recepty pacjenta

```sql
SELECT pacjent.`Imie`, pacjent.`Nazwisko`, wizyta.`ID_pacjenta`,
recepta.`Nazwa_lekarstwa`, recepta.`Sposob_podania`
FROM pacjent  LEFT JOIN wizyta ON wizyta.`ID_pacjenta` = pacjent.`ID_pacjenta`
INNER JOIN recepta ON recepta.`ID_wizyty` = wizyta.`ID_wizyty`
WHERE pacjent.`Imie` = '%s' AND pacjent.`Nazwisko` = '%s';
```
  
    
2. Wypisz wszystkich lekarzy na urlopie/nie na urlopie w kolejności alfabetycznej 

```sql
SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.Urlop
FROM pracownik  INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika
WHERE lekarz.Urlop = '%s'
ORDER BY Pracownik.Nazwisko ASC, Pracownik.Imie ASC;
```
  
    
3. Wyświtlenie danych kontaktowych
  
3.1 Wyświetlenie danych kontaktowych wszystkich lekarzy lub pacjentów 
```sql
SELECT Imie, Nazwisko, Telefon, Mail FROM %s;
```
3.2 Wyświetlenie danych kontaktowych konkretnego lekarza lub pacjenta
```sql
SELECT Imie, Nazwisko, Telefon, Mail FROM %s
WHERE Imie = '%s' AND Nazwisko = '%s';
```
  
    
4. Wyświetlenie godzin przyjęć lekarzy
  
4.1 Wyświetlenie godzin przyjęć wszystkich lekarzy
```sql
SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.ID_pracownika, gabinet.Godzina_rozpoczecia, gabinet.Godzina_zakonczenia
FROM pracownik  INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika
INNER JOIN gabinet ON gabinet.ID_pracownika = lekarz.ID_pracownika
ORDER BY Pracownik.Nazwisko ASC, Pracownik.Imie ASC;
```
4.2 Wyświetlenie godzin przyjęć konkretnego lekarza
```sql
SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.Specjalizacja, gabinet.Nr_gabinetu, gabinet.Pietro, gabinet.Godzina_rozpoczecia, gabinet.Godzina_zakonczenia
FROM pracownik  INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika
INNER JOIN gabinet ON gabinet.ID_pracownika = lekarz.ID_pracownika
WHERE pracownik.Imie = '%s' AND pracownik.Nazwisko = '%s';
```
  
    
5. Wyświetlenie wizyt
  
5.1 Wyświetlenie wszystkich wizyt posortowanych rosnąco po dacie
```sql
SELECT pracownik.Imie, pracownik.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty, gabinet.Nr_gabinetu
FROM pracownik  INNER JOIN wizyta ON wizyta.ID_pracownika = pracownik.ID_pracownika
INNER JOIN gabinet ON wizyta.ID_gabinetu = gabinet.ID_gabinetu
ORDER BY wizyta.data_wizyty ASC, wizyta.godzina_wizyty ASC;
```
5.2 Wyświetlenie wizyt konkretnego pracownika w konkretnym dniu
```sql
SELECT pracownik.Imie, pracownik.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty
FROM pracownik  INNER JOIN wizyta ON wizyta.ID_pracownika = pracownik.ID_pracownika
WHERE pracownik.Imie = '%s' AND pracownik.Nazwisko = '%s' AND wizyta.Data_wizyty = '%s'
ORDER BY wizyta.Godzina_wizyty ASC;
```
5.3 Wyświetlenie wizyt w konkretnym gabinecie
```sql
SELECT `pracownik`.`Imie`, `pracownik`.`Nazwisko`, `lekarz`.`Specjalizacja`, `wizyta`.`Data_wizyty`, `wizyta`.`Godzina_wizyty`, `pacjent`.`Imie`, `pacjent`.`Nazwisko`
FROM `pracownik` 
LEFT JOIN `lekarz` ON `lekarz`.`ID_pracownika` = `pracownik`.`ID_pracownika` 
LEFT JOIN `wizyta` ON `wizyta`.`ID_pracownika` = `pracownik`.`ID_pracownika` 
LEFT JOIN `gabinet` ON `wizyta`.`ID_gabinetu` = `gabinet`.`ID_gabinetu` 
LEFT JOIN `pacjent` ON `wizyta`.`ID_pacjenta` = `pacjent`.`ID_pacjenta`
WHERE `gabinet`.`Nr_gabinetu` = '11';
```
5.4 Wyświetlenie ilości wizyt pomiędzy konkretnymi datami oraz ich ilości 
```sql
SELECT Data_wizyty, COUNT(Data_wizyty) AS ‘Ilość’ FROM wizyta
WHERE Data_wizyty BETWEEN '%s' AND '%s'
GROUP BY Data_wizyty ORDER BY Data_wizyty ASC;

SELECT COUNT(*) FROM wizyta WHERE Data_wizyty BETWEEN '%s' AND '%s';
```
5.5 Wyświetlenie wizyt w konkretnym miesiącu oraz ich ilości
```sql
SELECT Data_wizyty, COUNT(Data_wizyty) AS ‘Ilość’ FROM wizyta
WHERE Data_wizyty LIKE '%s%s'
GROUP BY Data_wizyty ORDER BY Data_wizyty ASC;

SELECT COUNT(*) FROM wizyta WHERE Data_wizyty LIKE '%s%s';
```
    
6. Wyświetlenie historii wizyt pacjenta 
  
6.1 Posortowanych po dacie wizyty
```sql
SELECT pacjent.Imie, pacjent.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty FROM pacjent
INNER JOIN wizyta ON wizyta.ID_pacjenta = pacjent.ID_pacjenta
WHERE pacjent.Imie = '%s' AND pacjent.Nazwisko = '%s'
ORDER BY Wizyta.Data_wizyty ASC, Wizyta.Godzina_wizyty ASC;
```
6.2 W konkretnym przedziale czasowym
```sql
SELECT pacjent.Imie, pacjent.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty FROM pacjent
INNER JOIN wizyta ON wizyta.ID_pacjenta = pacjent.ID_pacjenta
WHERE pacjent.Imie = '%s' AND pacjent.Nazwisko = '%s' AND Data_wizyty BETWEEN '%s' AND '%s'
ORDER BY Wizyta.Data_wizyty ASC, Wizyta.Godzina_wizyty ASC;
```
  
    
7. Wyświetlenie wszystkich skierowań danego pacjenta
```sql
SELECT pacjent.Imie, pacjent.Nazwisko, wizyta.ID_pacjenta, skierowanie.ID_skierowania, skierowanie.Typ
FROM pacjent
INNER JOIN wizyta ON wizyta.ID_pacjenta = pacjent.ID_pacjenta
INNER JOIN skierowanie ON skierowanie.ID_wizyty = wizyta.ID_wizyty
WHERE pacjent.Imie = '%s' AND pacjent.Nazwisko = '%s';
```
  
    
8. Wyświetlenie zaplanowanych szczepień
  
8.1 Wyświetlenie wszystkich zaplanowanych szczepień
```sql
SELECT wizyta.Typ, pacjent.Imie, pacjent.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty, gabinet.Nr_gabinetu
FROM wizyta
INNER JOIN pacjent ON wizyta.ID_pacjenta = pacjent.ID_pacjenta
INNER JOIN gabinet ON wizyta.ID_gabinetu = gabinet.ID_gabinetu
WHERE wizyta.Typ = 'szczepienie'
ORDER BY Wizyta.Data_wizyty ASC, Wizyta.Godzina_wizyty ASC;
```
8.2 Wyświetlenie wszystkich zaplanowanych szczepień konkretnego pacjenta
```sql
SELECT wizyta.Typ, pacjent.Imie, pacjent.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty, gabinet.Nr_gabinetu
FROM wizyta
INNER JOIN pacjent ON wizyta.ID_pacjenta = pacjent.ID_pacjenta
INNER JOIN gabinet ON wizyta.ID_gabinetu = gabinet.ID_gabinetu
WHERE wizyta.Typ = 'szczepienie' AND pacjent.Imie = '%s' AND pacjent.Nazwisko = '%s'
ORDER BY Wizyta.Data_wizyty ASC, Wizyta.Godzina_wizyty ASC;
```
  
    
9. Wyświetlenie wszystkich lekarzy na stażu lub na pełnym etacie
```sql
SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.Etat FROM pracownik
INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika WHERE lekarz.Etat = '%s';
```
  
    
10. Wyświetlenie wszystkich osób w bazie
```sql
SELECT Imie, Nazwisko, Data_urodzenia
FROM Pacjent
UNION SELECT Imie, Nazwisko, Data_urodzenia
FROM Pracownik
ORDER BY Data_urodzenia;
```
  
    
11. Wyszukaj numer PESEL i datę urodzenia konkretnego pacjenta
```sql
SELECT pacjent.Imie, pacjent.Nazwisko, pacjent.Data_urodzenia, pacjent.Pesel
FROM pacjent
WHERE pacjent.Imie = '%s' AND pacjent.Nazwisko = '%s';
```
  
    
12. Zliczenie pracowników o danej funkcji tj. lekarzy, pielęgniarek i recepcjonistek
```sql
SELECT Pracownik.Funkcja AS 'Zawod pracownika',
COUNT(Pracownik.funkcja) AS 'Ilosc pracownikow'
FROM Pracownik
GROUP BY Pracownik.Funkcja
ORDER BY Pracownik.Funkcja ASC;
```

13. Zlicz lekarzy danej specjalizacji
13.1 Wyświetl ilość lekarzy wszystkich specjalizacji
```sql
SELECT Lekarz.Specjalizacja, COUNT(Lekarz.Specjalizacja) AS 'Ilość'
FROM Lekarz
GROUP BY Lekarz.Specjalizacja
ORDER BY Lekarz.Specjalizacja ASC;
```
13.2 Wyświetl ilość lekarzy konkretnej specjalizacji
```sql
SELECT Lekarz.Specjalizacja, COUNT(Lekarz.Specjalizacja) AS 'Ilość'
FROM Lekarz
WHERE Lekarz.Specjalizacja = '%s'
GROUP BY Lekarz.Specjalizacja;
```

### Sekcja zarządzania danymi


1. Zarejestruj pacjenta
  
a) Sprawdzenie czy pacjent posiada ubezpieczenie (gdy nie posiada, nie może zarejestrować się do lekarza) oraz jego ID w bazie
```sql
SELECT ubezpieczenie , ID_pacjenta FROM Pacjent WHERE Imie='%s' AND Nazwisko='%s';
```
b) Sprawdzenie, czy lekarz jest na urlopie oraz wypisanie ID pracownika i ID gabinetu
```sql
SELECT lekarz.`Urlop`, gabinet.`ID_pracownika`, gabinet.`ID_gabinetu` FROM pracownik
INNER JOIN lekarz ON lekarz.`ID_pracownika` = pracownik.`ID_pracownika`
INNER JOIN gabinet ON gabinet.`ID_pracownika` = lekarz.`ID_pracownika`
WHERE pracownik.`Imie` = '%s' AND pracownik.`Nazwisko` = '%s';
```
c) Sprawdzenie czy jest wolny termin (jeżeli jest zajęty zwrócenie 1, jeżeli nie zwrócenie 0)
```sql
SELECT COUNT(wizyta.`ID_pracownika`) FROM wizyta
WHERE wizyta.`ID_pracownika` = '%s' AND wizyta.`Godzina_wizyty` = '%s' AND
wizyta.`Data_wizyty` = '%s';
```
d) Zliczenie ilości wizyt
```sql
SELECT COUNT(ID_wizyty) FROM Wizyta;
```
e) Wstawienie danych do tabeli wizyta
```sql
INSERT INTO wizyta VALUES(%s, '%s', %s, %s, %s, '%s', '%s');
```

2. Dodanie osoby do bazy
  
a) Obliczenie ilości osób w tabeli Pracownik lub w tabeli Pacjent
```sql
SELECT COUNT(*) FROM %s;
```
b) Dodanie danych do odpowiedniej tabeli, czyli Pracownik lub Pacjent, jeśli Pracownik był lekarzem to dodaj dane w tabeli Lekarz
```sql
INSERT INTO pracownik (ID_pracownika, Imie, Nazwisko, Data_urodzenia, Pesel,
Miejsce_zamieszkania, Telefon, Mail, Funkcja)
VALUES (%s, '%s', '%s', '%s', '%s', '%s', %s, '%s', '%s');

INSERT INTO pacjent (ID_pacjenta, Imie, Nazwisko, Data_urodzenia, Pesel, Miejsce_zamieszkania,
Telefon, Mail, Ubezpieczenie) VALUES(%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');

INSERT INTO `lekarz` (`ID_pracownika`, `Specjalizacja`, `Staz_pracy`, `Etat`, `Urlop`)
VALUES(%s, '%s', %s, '%s', 0);
```

3. Modyfikacja danych kontaktowych pracownika lub pacjenta
Pozwala na wybór tabeli, kolumny oraz danych jakie są modyfikowane.
```sql
UPDATE %s SET %s = '%s' WHERE Imie = '%s' AND Nazwisko = '%s';
```


4. Usuń wizytę z bazy  
Funkcjonalność można wykorzystać w  razie gdyby ktoś chciał odwołać wizytę lub gdyby pacjent już nie był w tej przychodni i należałoby usunąć jego dane. Dzieje się to przez usuwanie odpowiednich encji z bazy danych.
  
a) Sprawdzenie ID wizyty
```sql
SELECT ID_wizyty FROM wizyta WHERE id_pacjenta = (SELECT ID_pacjenta FROM pacjent WHERE Imie = '%s'
AND Nazwisko = '%s') AND Data_wizyty = '%s' AND Godzina_wizyty = '%s';
```
b) Usunięcie skierowania o konkretnym ID wizyty (jeśli istnieje)
```sql
DELETE FROM Skierowanie WHERE ID_wizyty = '%s';
```
c) Usunięcie recepty o konkretnym ID wizyty (jeśli istnieje)
```sql
DELETE FROM Recepta WHERE ID_wizyty = '%s';
```
d) Usunięcie wizyty
```sql
DELETE FROM Wizyta WHERE ID_wizyty = '%s';
```

5. Wpisanie urlopu lekarzowi
```sql
UPDATE Lekarz SET Lekarz.urlop = 1 WHERE (SELECT ID_pracownika from Pracownik WHERE Pracownik.Imie
= '%s' AND Pracownik.Nazwisko = '%s') = ID_pracownika;
```

6. Dodaj skierowanie
6.1 Sprawdź ID wizyty do której chcesz dodać skierowanie
```sql
SELECT ID_wizyty FROM wizyta WHERE id_pacjenta = (SELECT ID_pacjenta FROM pacjent
WHERE Imie = '%s' AND Nazwisko = '%s') AND Data_wizyty = '%s' AND Godzina_wizyty = '%s';
```
6.2 Oblicz ID skierowania
```sql
SELECT COUNT(*) FROM Skierowanie;
```
6.3 Dodanie danych 
```sql
INSERT INTO `skierowanie` (`ID_skierowania`, `ID_wizyty`, `Typ`) VALUES(%s, %s, '%s');
```

7. Dodaj receptę
7.1 Sprawdź ID wizyty do której chcesz dodać receptę
```sql
SELECT ID_wizyty FROM wizyta WHERE id_pacjenta = (SELECT ID_pacjenta FROM pacjent
WHERE Imie = '%s' AND Nazwisko = '%s') AND Data_wizyty = '%s' AND Godzina_wizyty = '%s';
```
7.2 Oblicz ID recepty
```sql
SELECT COUNT(*) FROM Recepta;
```
7.3 Dodanie danych
```sql
INSERT INTO `recepta` (`ID_recepty`, `Nazwa_lekarstwa`, `Sposob_podania`, `ID_wizyty`)
VALUES(%s, '%s', '%s', %s);
```

8. Modyfikuj ubezpieczenie
8.1 Sprawdź czy pacjent ma ubezpieczenie (0 lub 1)
```sql
SELECT Ubezpieczenie FROM Pacjent WHERE Imie = '%s' AND Nazwisko = '%s';
```
8.2 Zmień ubezpiecznie na przeciwne 
```sql
UPDATE Pacjent SET Ubezpieczenie = 1 WHERE Imie = '%s' AND Nazwisko = '%s';

UPDATE Pacjent SET Ubezpieczenie = 0 WHERE Imie = '%s' AND Nazwisko = '%s';
```

  
    
## Aplikacja
Aplikacja oparta jest o menu wyboru podzielone na dwie sekcje - sekcję sprawdzania danych i sekcję zarządzania danymi. Z poziomu menu możliwe jest także zamknięcie aplikacji. W poszczególnych sekcjach istnieje możliwość wybrania konkretnych funkcjonalności oraz cofnięcie się do menu wyboru sekcji. 
  
"Sekcja sprawdzania danych" polega na wypisywaniu danych zawartych w bazie przychodni lekarskiej. Pozwala między innymi na wypisywanie informacji dotyczących wizyt, lekarzy i pacjentów, pozwala na przeglądanie wypisanych recept i skierowań. 
  
"Sekcja zarządzania danymi" pozwala na robienie zmian w bazie poprzez aktualizacje czy dodawanie nowych danych do tabel. Ta sekcja pozwala między innymi na dodawanie wizyt, recept i skierowań, dodawanie urlopu lekarzowi lub pozwala na usuwanie wizyt z bazy. 
  
Obsługa aplikacji odbywa się z poziomu terminala. Aplikacja jest interaktywna z użytkownikiem i pozwala na wpisywanie potrzebnych danych przez użytkownika. Istnieje łatwa możliwość rozbudowania aplikacji o nowe funkcjonalności.
  
    
Przykładowa implementacja niektórych funkcjonalności:
  
1. Dodawanie skierowania pacjentowi 
```py
def dodaj_skierowanie(imie,nazwisko,data,godzina):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT ID_wizyty FROM wizyta WHERE id_pacjenta = (SELECT ID_pacjenta FROM pacjent WHERE Imie = '%s' " \
                  "AND Nazwisko = '%s') AND Data_wizyty = '%s' AND Godzina_wizyty = '%s';" % (
                  imie, nazwisko, data, godzina)
            cursor.execute(sql)
            id_wizyty = cursor.fetchone()
            id_wizyty = int(id_wizyty[0])

            sql = "SELECT COUNT(*) FROM Skierowanie;"
            cursor.execute(sql)
            id_skierowania = cursor.fetchone()
            id_skierowania = int(id_skierowania[0]) + 1

            do_kogo = input('Podaj typ skierowania: ')

            sql = "INSERT INTO skierowanie (ID_skierowania, ID_wizyty, Typ)" \
              "VALUES(%s, %s, '%s');" % (id_skierowania, id_wizyty, do_kogo)
            cursor.execute(sql)
            connection.commit()

    finally:
        connection.close()
```
Funkcja wymaga podania przez użytkownika imienia i nazwiska pacjenta oraz daty i godziny podczas której wystawiono skierowanie. Funkcja sama sprawdza odpowiednie ID wizyty oraz wyznacza nowe ID skierowania. Po podaniu typu skierowania, np. "do kardiologa" lekarz jest w stanie dodać skierowanie do bazy.
  
    
2. Sprawdzenie wizyt lekarza w danym dniu
```py
def wizyty_lekarza_w_dniu(imie_lekarza, nazwisko_lekarza, dzien):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT pracownik.Imie, pracownik.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty " \
                  "FROM pracownik  INNER JOIN wizyta ON wizyta.ID_pracownika = pracownik.ID_pracownika " \
                  "WHERE pracownik.Imie = '%s' AND pracownik.Nazwisko = '%s' AND wizyta.Data_wizyty = '%s' " \
                  "ORDER BY wizyta.Godzina_wizyty ASC;" % (imie_lekarza, nazwisko_lekarza, dzien)

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1], row[2], row[3])

    finally:
        connection.close()
```
Funkcja pozwala na sprawdzenie wizyt lekarza w danym dniu po wpisaniu jego imienia i nazwiska oraz żądanego dnia. Wizyty segregowane są godzinami, zatem wyświetlą się w bazie po kolei.
    

## Dodatkowe uwagi
W tabeli Lekarz w kolumnie Urlop: 
- 1 oznacza, że lekarz jest na urlopie
- 0 oznacza, że lekarz nie jest na urlopie
  
W tabeli Pacjent w kolumnie Ubezpieczenie:
- 1 oznacza, że pacjent posiada ubezpieczenie i może zarejestrować się na wizytę
- 0 oznacza, że pacjent nie ma ubezpieczenia i nie może zarejestrować się na wizytę
