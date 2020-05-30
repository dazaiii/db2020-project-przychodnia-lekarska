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
INSERT INTO Pacjent VALUES('3','Maciej','Glowczyk','1981-04-12','81041212345','Tarnow','346283716','maciej_glowczyk@mail.com', 1);
INSERT INTO Pacjent VALUES('4','Krzysztof','Rabczewski','1969-02-05','69020538261','Oswiecim','609752817','k_rabczewski@mail.com', 1);
INSERT INTO Pacjent VALUES('5','Krzysztof','Nowakowski','1978-11-05','78110509675','Krakow','890765876','k_nowakowski@mail.com', 1);
INSERT INTO Pacjent VALUES('6','Mikolaj','Mikolajowski','1990-12-11','90121178256','Krakow','6009876547','mikolajowski@mail.com', 1);
INSERT INTO Pacjent VALUES('7','Mariusz','Budzyn','1929-01-01','21010176543','Niepolomice','789654321','budzyn@mail.com', 1);
INSERT INTO Pacjent VALUES('8','Justyna','Kowal','1978-02-05','78020512765','Krakow','60098456728','justyna_kowal@mail.com', 1);
INSERT INTO Pacjent VALUES('8','Zofia','Piotrowska','2001-10-10','01101076578','Niepolomice','789654678','piotrowksa@mail.com', 1);
INSERT INTO Pacjent VALUES('9','Joanna','Maciszewska','1998-12-10','98121076238','Wieliczka','654789678','maciszewska@mail.com', 0);
INSERT INTO Pacjent VALUES('10','Zygmunt','Wolak','1950-04-27','50042789765','Krakow','654789654','zygmunt_wolak@mail.com', 1);

INSERT INTO Pracownik VALUES('1','Piotr','Majewski','1940-02-11','40021167854','Krakow','123456789','majewski@mail.com','Lekarz');
INSERT INTO Pracownik VALUES('2','Krzysztof','Jarczewski','1959-02-11','59021112345','Krakow','456787658','kj@mail.com','Lekarz');
INSERT INTO Pracownik VALUES('3','Karolina','Malinowska','1967-04-04','67040454678','Oswiecim','567865456','malinowska@mail.com','Lekarz');
INSERT INTO Pracownik VALUES('4','Malwina','Janiszewska','1987-05-20','87052087659','Krakow','567876908','janiszewska@mail.com','Lekarz');
INSERT INTO Pracownik VALUES('5','Janina','Wojtaszewska','1969-03-15','69031512345','Wieliczka','123456789','wojtaszewska@mail.com','Pielegniarka');
INSERT INTO Pracownik VALUES('5','Edyta','Wojcik','1970-05-15','70051512345','Tarnow','123456789','edyta_wojcik@mail.com','Pielegniarka');

INSERT INTO Lekarz VALUES('1','Kardiolog','1','staz',0);
INSERT INTO Lekarz VALUES('2','Dermatolog','10','pełny',0);
INSERT INTO Lekarz VALUES('3','Pediatra','12','pełny',1);
INSERT INTO Lekarz VALUES('4','Neurolog','5','pełny',0);

INSERT INTO Gabinet VALUES('5','8','2','2020-05-20','20:50:00','1');

INSERT INTO Recepta VALUES('1','Ibuprofen','Nurofen','a','b','c');

INSERT INTO Uwagi VALUES('1','Skierowanie','1','1','Lekarz');

INSERT INTO Wizyta VALUES('1','Badanie','1','1','5','1','1',"2020-05-20",'20:50:00');

/* Foreign key */

ALTER TABLE Uwagi ADD FOREIGN KEY (ID_wizyty) REFERENCES Wizyta(ID_wizyty);

/* Uzytkownicy */

DROP USER IF EXISTS przychodniadb@localhost;

CREATE USER przychodniadb@localhost IDENTIFIED BY 'przychodniadb';
GRANT ALL PRIVILEGES ON przychodniadb.* TO przychodniadb@localhost;
FLUSH PRIVILEGES;