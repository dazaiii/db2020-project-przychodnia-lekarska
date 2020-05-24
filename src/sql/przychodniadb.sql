CREATE DATABASE IF NOT EXISTS przychodniadb;

USE przychodniadb;

/* **************** Tworzenie Tabel ********************* */

CREATE TABLE Pacjent(
    ID_pacjenta int,
    Imie varchar(50),
    Nazwisko varchar(50),
    Data_urodzenia DATE,
    Pesel int NOT NULL,
    Miejsce_zamieszkania varchar(50),
    Telefon int,
    Mail varchar(50),
    Ubezpieczenie BIT,
    PRIMARY KEY (ID_pacjenta)
);

CREATE TABLE Pracownik(
    ID_pracownika int,
    Imie varchar(50),
    Nazwisko varchar(50),
    Pesel int NOT NULL,
    Miejsce_zamieszkania varchar(50),
    Telefon int,
    Mail varchar(50),
    Funkcja varchar(50),
    PRIMARY KEY (ID_pracownika)
);

CREATE TABLE Lekarz(
    ID_pracownika int,
    Specjalizacja varchar(50),
    Staz_pracy int,
    Etat varchar(50),
    Urlop BIT,
    PRIMARY KEY (ID_pracownika),
    FOREIGN KEY (ID_pracownika) REFERENCES Pracownik(ID_pracownika)
);

CREATE TABLE Gabinet(
    ID_gabinetu int,
    Nr_gabinetu int,
    Pietro int,
    Dzien_tygodnia DATE,
    Godziny_przyjec TIME,
    ID_pracownika int,
    PRIMARY KEY (ID_gabinetu),
    FOREIGN KEY (ID_pracownika) REFERENCES Pracownik(ID_pracownika)
);

CREATE TABLE Recepta(
    ID_recepty int,
    Lek1 varchar(50),
    Lek2 varchar(50),
    Lek3 varchar(50),
    Lek4 varchar(50),
    Lek5 varchar(50),
    PRIMARY KEY (ID_recepty),
);

CREATE TABLE Uwagi(
    ID_uwagi int,
    Typ varchar(50),
    ID_wizyty int,
    ID_pracownika int,
    Funkcja varchar(50);
    PRIMARY KEY (ID_uwagi),
    FOREIGN KEY (ID_pracownika) REFERENCES Pracownik(ID_pracownika)
);

CREATE TABLE Wizyta(
    ID_wizyty int,
    Typ varchar(50),
    ID_pracownika int,
    ID_pacjenta int,
    ID_gabinetu int,
    ID_recepty int,
    ID_uwagi int,
    Data_wizyty DATE,
    Godzina_wizyty TIME,
    PRIMARY KEY (ID_wizyty),
    FOREIGN KEY (ID_pacjenta) REFERENCES Pacjent(ID_pacjenta),
    FOREIGN KEY (ID_pracownika) REFERENCES Pracownik(ID_pracownika),
    FOREIGN KEY (ID_gabinetu) REFERENCES Gabinet(ID_gabinetu),
    FOREIGN KEY (ID_recepty) REFERENCES Recepta(ID_recepty),
    FOREIGN KEY (ID_uwagi) REFERENCES Uwagi(ID_uwagi)
);

ALTER TABLE Uwagi ADD FOREIGN KEY (ID_wizyty) REFERENCES Wizyta(ID_wizyty);
