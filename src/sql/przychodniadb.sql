DROP DATABASE IF EXISTS przychodniadb;

CREATE DATABASE IF NOT EXISTS przychodniadb;

USE przychodniadb;

/* **************** Tworzenie Tabel ********************* */

CREATE TABLE Pacjent(
    ID_pacjenta int,
    Imie varchar(50),
    Nazwisko varchar(50),
    Data_urodzenia DATE,
    Pesel varchar(10),
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
    Data_urodzenia DATE,
    Pesel varchar(10),
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
    PRIMARY KEY (ID_recepty)
);

CREATE TABLE Uwagi(
    ID_uwagi int,
    Typ varchar(50),
    ID_wizyty int,
    ID_pracownika int,
    Funkcja varchar(50),
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

/* Dodawanie */
INSERT INTO Pacjent VALUES('1','Adam','Nowak','1920-02-11','20021112345','Krakow','123456789','an@mail.com',0);
INSERT INTO Pacjent VALUES('2','Janusz','Kowalski','1960-05-11','60051112345','Krakow','123456789','jk@mail.com',1);

INSERT INTO Pracownik VALUES('1','Piotr','Madao','1940-02-11','20021112345','Krakow','123456789','madao@mail.com','Lekarz');
INSERT INTO Pracownik VALUES('2','Krzysztof','Jarek','1959-02-11','59021112345','Krakow','123456789','kj@mail.com','Pielegniarka');

INSERT INTO Lekarz VALUES('1','Kardiolog','1','pełny',0);

INSERT INTO Gabinet VALUES('5','8','2','2020-05-20','20:50:00','1');

INSERT INTO Recepta VALUES('1','Ibuprofen','Nurofen','a','b','c');

INSERT INTO Uwagi VALUES('1','Skierowanie','1','1','Lekarz');

INSERT INTO Wizyta VALUES('1','Badanie','1','1','5','1','1',"2020-05-20",'20:50:00');

/* Foreign key */

ALTER TABLE Uwagi ADD FOREIGN KEY (ID_wizyty) REFERENCES Wizyta(ID_wizyty);

/* Uzytkownicy */

DROP USER IF EXISTS przychodniadb@localhost;

CREATE USER przychodniadb@localhost IDENTIFIED BY 'Zaq12wsx';
GRANT ALL PRIVILEGES ON przychodniadb.* TO przychodniadb@localhost;