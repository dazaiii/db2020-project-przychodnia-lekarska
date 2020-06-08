/* 1.Dodaj receptę dla konkretnej wizyty */

INSERT INTO recepta VALUES (21, "Apap", "Doustnie", 1);

/* 2.Dodaj pacjenta do bazy */
INSERT INTO pacjent VALUES (31, "Mateusz", "Nowak", 1993-03-10, "93031039487", "Kraków", 674356409, "nowak_mateusz@mail.com", 1);

/* 3.Wypisz wszystkich lekarzy na urlopie */

SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.Urlop
FROM pracownik
INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika
WHERE lekarz.Urlop = '1';

/* 4.Wypisz godziny przyjęć danego lekarza */

SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.ID_pracownika, gabinet.Godzina_rozpoczecia, gabinet.Godzina_zakonczenia
FROM pracownik
INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika
INNER JOIN gabinet ON gabinet.ID_pracownika = lekarz.ID_pracownika;

/* 5.Wypisz dane kontaktowe danego lekarza */

SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.Specjalizacja, pracownik.Telefon, pracownik.Mail
FROM pracownik
INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika
WHERE pracownik.Imie = 'Krzysztof' AND pracownik.Nazwisko = 'Jarczewski';

/* 6.Wypisz wizyty danego lekarza w danym dniu (To było dla piotra majewskiego, można mu dać więcej wizyt 08.06 aby było widać w programie) */

SELECT pracownik.Imie, pracownik.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty
FROM pracownik
INNER JOIN wizyta ON wizyta.ID_pracownika = pracownik.ID_pracownika
WHERE pracownik.Imie = 'Piotr' AND pracownik.Nazwisko = 'Majewski' AND wizyta.Data_wizyty = '2020-06-08';

/* 7.Wypisz wizyty w danym gabinecie */

SELECT gabinet.Nr_gabinetu, gabinet.Pietro, wizyta.ID_wizyty, pacjent.Imie, pacjent.Nazwisko
FROM gabinet
LEFT JOIN wizyta ON wizyta.ID_gabinetu = gabinet.ID_gabinetu
LEFT JOIN pacjent ON wizyta.ID_pacjenta = pacjent.ID_pacjenta
WHERE gabinet.Nr_gabinetu = '31';

/* 8.Wyświetl recepty danego pacjenta */

SELECT pacjent.Imie, pacjent.Nazwisko, wizyta.ID_pacjenta, recepta.Nazwa_lekarstwa, recepta.Sposob_podania
FROM pacjent
LEFT JOIN wizyta ON wizyta.ID_pacjenta = pacjent.ID_pacjenta
LEFT JOIN recepta ON recepta.ID_wizyty = wizyta.ID_wizyty
WHERE pacjent.Imie = 'Adam' AND pacjent.Nazwisko = 'Nowak';
