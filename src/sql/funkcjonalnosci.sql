/* 1. Zarejestruj pacjenta */

SELECT ubezpieczenie , ID_pacjenta FROM Pacjent WHERE Imie='%s' AND Nazwisko='%s'

SELECT `lekarz`.`Urlop`, `gabinet`.`ID_pracownika`, `gabinet`.`ID_gabinetu` FROM `pracownik`
INNER JOIN `lekarz` ON `lekarz`.`ID_pracownika` = `pracownik`.`ID_pracownika`
INNER JOIN `gabinet` ON `gabinet`.`ID_pracownika` = `lekarz`.`ID_pracownika`
WHERE `pracownik`.`Imie` = '%s' AND `pracownik`.`Nazwisko` = '%s';

SELECT COUNT(`wizyta`.`ID_pracownika`) FROM `wizyta`
WHERE `wizyta`.`ID_pracownika` = '%s' AND `wizyta`.`Godzina_wizyty` = '%s' AND
`wizyta`.`Data_wizyty` = '%s';

SELECT COUNT(ID_wizyty) FROM Wizyta;"

INSERT INTO `wizyta` VALUES(%s, '%s', %s, %s, %s, '%s', '%s');

/* 2. Wyswietl receptę */

SELECT `pacjent`.`Imie`, `pacjent`.`Nazwisko`, `wizyta`.`ID_pacjenta`,
`recepta`.`Nazwa_lekarstwa`, `recepta`.`Sposob_podania`
FROM `pacjent`  LEFT JOIN `wizyta` ON `wizyta`.`ID_pacjenta` = `pacjent`.`ID_pacjenta`
LEFT JOIN `recepta` ON `recepta`.`ID_wizyty` = `wizyta`.`ID_wizyty`
WHERE `pacjent`.`Imie` = '%s' AND `pacjent`.`Nazwisko` = '%s';

/* 3. Wypisz lekarzy na urlopie/nie na urlopie */

SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.Urlop
FROM pracownik  INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika
WHERE lekarz.Urlop = '%s'
ORDER BY Pracownik.Nazwisko ASC, Pracownik.Imie ASC;

/* 4. Wyświetl dane kontaktowe */

SELECT Imie, Nazwisko, Telefon, Mail FROM %s;

SELECT Imie, Nazwisko, Telefon, Mail FROM %s
WHERE Imie = '%s' AND Nazwisko = '%s';

/* 5. Wyświetl godziny przyjęć lekarzy */

SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.ID_pracownika, gabinet.Godzina_rozpoczecia, gabinet.Godzina_zakonczenia
FROM pracownik  INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika
INNER JOIN gabinet ON gabinet.ID_pracownika = lekarz.ID_pracownika
ORDER BY Pracownik.Nazwisko ASC, Pracownik.Imie ASC;

SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.Specjalizacja, gabinet.Nr_gabinetu, gabinet.Pietro, gabinet.Godzina_rozpoczecia, gabinet.Godzina_zakonczenia
FROM pracownik  INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika
INNER JOIN gabinet ON gabinet.ID_pracownika = lekarz.ID_pracownika
WHERE pracownik.Imie = '%s' AND pracownik.Nazwisko = '%s';

/* 6. Dodaj osobę do bazy */

SELECT COUNT(*) FROM %s;

INSERT INTO `pacjent` (`ID_pacjenta`, `Imie`, `Nazwisko`, `Data_urodzenia`, `Pesel`, `Miejsce_zamieszkania`,
`Telefon`, `Mail`, `Ubezpieczenie`) VALUES(%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');

INSERT INTO `pracownik` (`ID_pracownika`, `Imie`, `Nazwisko`, `Data_urodzenia`, `Pesel`,
Miejsce_zamieszkania`, `Telefon`, `Mail`, `Funkcja`)
VALUES (%s, '%s', '%s', '%s', '%s', '%s', %s, '%s', '%s');

/* 7. Wyświetl wizyty */

SELECT pracownik.Imie, pracownik.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty, gabinet.Nr_gabinetu
FROM pracownik  INNER JOIN wizyta ON wizyta.ID_pracownika = pracownik.ID_pracownika
INNER JOIN gabinet ON wizyta.ID_gabinetu = gabinet.ID_gabinetu
ORDER BY wizyta.data_wizyty ASC, wizyta.godzina_wizyty ASC;

SELECT pracownik.Imie, pracownik.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty
FROM pracownik  INNER JOIN wizyta ON wizyta.ID_pracownika = pracownik.ID_pracownika
WHERE pracownik.Imie = '%s' AND pracownik.Nazwisko = '%s' AND wizyta.Data_wizyty = '%s'
ORDER BY wizyta.Godzina_wizyty ASC;

SELECT gabinet.Nr_gabinetu, gabinet.Pietro, wizyta.ID_wizyty, pacjent.Imie, pacjent.Nazwisko
FROM gabinet
LEFT JOIN wizyta ON wizyta.ID_gabinetu = gabinet.ID_gabinetu
LEFT JOIN pacjent ON wizyta.ID_pacjenta = pacjent.ID_pacjenta WHERE gabinet.Nr_gabinetu = '%s';

/* 8. Wyświetl historię wizyt pacjenta */

SELECT pacjent.Imie, pacjent.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty FROM pacjent
INNER JOIN wizyta ON wizyta.ID_pacjenta = pacjent.ID_pacjenta
WHERE pacjent.Imie = '%s' AND pacjent.Nazwisko = '%s'
ORDER BY Wizyta.Data_wizyty ASC, Wizyta.Godzina_wizyty ASC;

/* 9. Wyświetl wszystkie skierowania danego pacjenta */

SELECT pacjent.Imie, pacjent.Nazwisko, wizyta.ID_pacjenta, skierowanie.ID_skierowania, skierowanie.Typ
FROM pacjent
INNER JOIN wizyta ON wizyta.ID_pacjenta = pacjent.ID_pacjenta
INNER JOIN skierowanie ON skierowanie.ID_wizyty = wizyta.ID_wizyty
WHERE pacjent.Imie = '%s' AND pacjent.Nazwisko = '%s';