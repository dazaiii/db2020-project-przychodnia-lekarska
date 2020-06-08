SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Baza danych: `przychodnia`
--
CREATE DATABASE IF NOT EXISTS `przychodniadb` DEFAULT CHARACTER SET utf8 COLLATE utf8_polish_ci;
USE `przychodniadb`;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `gabinet`
--

CREATE TABLE `gabinet` (
  `ID_gabinetu` int(10) NOT NULL,
  `Nr_gabinetu` int(10) NOT NULL,
  `Pietro` int(10) NOT NULL,
  `Godzina_rozpoczecia` time NOT NULL,
  `Godzina_zakonczenia` time NOT NULL,
  `ID_pracownika` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `gabinet`
--

INSERT INTO `gabinet` VALUES(1, 10, 1, '08:00:00', '16:00:00', 1);
INSERT INTO `gabinet` VALUES(2, 11, 1, '09:30:00', '17:30:00', 2);
INSERT INTO `gabinet` VALUES(3, 20, 2, '08:30:00', '16:00:00', 3);
INSERT INTO `gabinet` VALUES(4, 21, 2, '08:00:00', '14:00:00', 4);
INSERT INTO `gabinet` VALUES(5, 31, 3, '08:00:00', '17:00:00', 8);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `lekarz`
--

CREATE TABLE `lekarz` (
  `ID_pracownika` int(10) NOT NULL,
  `Specjalizacja` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Staz_pracy` int(10) NOT NULL,
  `Etat` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Urlop` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `lekarz`
--

INSERT INTO `lekarz` VALUES(1, 'Kardiolog', 1, 'staz', 0);
INSERT INTO `lekarz` VALUES(2, 'Dermatolog', 10, 'pełny', 0);
INSERT INTO `lekarz` VALUES(3, 'Pediatra', 12, 'pełny', 1);
INSERT INTO `lekarz` VALUES(4, 'Neurolog', 5, 'pełny', 0);
INSERT INTO `lekarz` VALUES(8, 'Ogolny', 15, 'pelny', 0);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pacjent`
--

CREATE TABLE `pacjent` (
  `ID_pacjenta` int(10) NOT NULL,
  `Imie` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Nazwisko` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Data_urodzenia` date NOT NULL,
  `Pesel` varchar(11) COLLATE utf8_polish_ci NOT NULL,
  `Miejsce_zamieszkania` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Telefon` int(10) NOT NULL,
  `Mail` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Ubezpieczenie` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `pacjent`
--

INSERT INTO `pacjent` VALUES(1, 'Adam', 'Nowak', '1920-02-11', '20021112345', 'Kraków', 123456789, 'an@mail.com', 0);
INSERT INTO `pacjent` VALUES(2, 'Janusz', 'Kowalski', '1960-05-11', '60051112345', 'Kraków', 123456789, 'jk@mail.com', 1);
INSERT INTO `pacjent` VALUES(3, 'Maciej', 'Glowczyk', '1981-04-12', '81041212345', 'Tarnów', 346283716, 'maciej_glowczyk@mail.com', 1);
INSERT INTO `pacjent` VALUES(4, 'Krzysztof', 'Rabczewski', '1969-02-05', '69020538261', 'Oświęcim', 609752817, 'k_rabczewski@mail.com', 1);
INSERT INTO `pacjent` VALUES(5, 'Krzysztof', 'Nowakowski', '1978-11-05', '78110509675', 'Kraków', 890765876, 'k_nowakowski@mail.com', 1);
INSERT INTO `pacjent` VALUES(6, 'Mikolaj', 'Mikolajowski', '1990-12-11', '90121178256', 'Kraków', 2147483647, 'mikolajowski@mail.com', 1);
INSERT INTO `pacjent` VALUES(7, 'Mariusz', 'Budzyn', '1929-01-01', '21010176543', 'Niepołomice', 789654321, 'budzyn@mail.com', 1);
INSERT INTO `pacjent` VALUES(8, 'Justyna', 'Kowal', '1978-02-05', '78020512765', 'Kraków', 2147483647, 'justyna_kowal@mail.com', 1);
INSERT INTO `pacjent` VALUES(9, 'Zofia', 'Piotrowska', '2001-10-10', '01101076578', 'Niepołomice', 789654678, 'piotrowksa@mail.com', 1);
INSERT INTO `pacjent` VALUES(10, 'Joanna', 'Maciszewska', '1998-12-10', '98121076238', 'Wieliczka', 654789678, 'maciszewska@mail.com', 0);
INSERT INTO `pacjent` VALUES(11, 'Zygmunt', 'Wolak', '1950-04-27', '50042789765', 'Kraków', 654789654, 'zygmunt_wolak@mail.com', 1);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pracownik`
--

CREATE TABLE `pracownik` (
  `ID_pracownika` int(11) NOT NULL,
  `Imie` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Nazwisko` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Data_urodzenia` date NOT NULL,
  `Pesel` varchar(11) COLLATE utf8_polish_ci NOT NULL,
  `Miejsce_zamieszkania` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Telefon` int(10) NOT NULL,
  `Mail` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Funkcja` varchar(50) COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `pracownik`
--

INSERT INTO `pracownik` VALUES(1, 'Piotr', 'Majewski', '1940-02-11', '40021167854', 'Kraków', 123456789, 'majewski@mail.com', 'Lekarz');
INSERT INTO `pracownik` VALUES(2, 'Krzysztof', 'Jarczewski', '1959-02-11', '59021112345', 'Kraków', 456787658, 'kj@mail.com', 'Lekarz');
INSERT INTO `pracownik` VALUES(3, 'Karolina', 'Malinowska', '1967-04-04', '67040454678', 'Oświęcim', 567865456, 'malinowska@mail.com', 'Lekarz');
INSERT INTO `pracownik` VALUES(4, 'Malwina', 'Janiszewska', '1987-05-20', '87052087659', 'Kraków', 567876908, 'janiszewska@mail.com', 'Lekarz');
INSERT INTO `pracownik` VALUES(5, 'Janina', 'Wojtaszewska', '1969-03-15', '69031512345', 'Wieliczka', 123456789, 'wojtaszewska@mail.com', 'Pielegniarka');
INSERT INTO `pracownik` VALUES(6, 'Edyta', 'Wojcik', '1970-05-15', '70051512345', 'Tarnów', 123456789, 'edyta_wojcik@mail.com', 'Pielegniarka');
INSERT INTO `pracownik` VALUES(7, 'Julia', 'Kowalewska', '1971-10-15', '71101512328', 'Kraków', 567387659, 'kowalewska_julia@mail.com', 'Recepcjonistka');
INSERT INTO `pracownik` VALUES(8, 'Marian', 'Gorski', '1988-08-22', '87052288659', 'Kraków', 567876908, 'mgorski@mail.com', 'Lekarz');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `recepta`
--

CREATE TABLE `recepta` (
  `ID_recepty` int(10) NOT NULL,
  `Nazwa_lekarstwa` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Sposob_podania` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `ID_wizyty` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `recepta`
--

INSERT INTO `recepta` VALUES(1, 'Ibuprom', 'Doustnie', 1);
INSERT INTO `recepta` VALUES(2, 'Ibupm', 'Doustnie', 2);
INSERT INTO `recepta` VALUES(3, 'Nurofen', 'Doustnie', 3);
INSERT INTO `recepta` VALUES(5, 'Anpan', 'Doustnie', 4);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `uwagi`
--

CREATE TABLE `uwagi` (
  `ID_uwagi` int(10) NOT NULL,
  `Typ` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `ID_wizyty` int(10) NOT NULL,
  `Funkcja` varchar(50) COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `uwagi`
--

INSERT INTO `uwagi` VALUES(1, 'Skierowanie', 1, 'Do kardiologa');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `wizyta`
--

CREATE TABLE `wizyta` (
  `ID_wizyty` int(10) NOT NULL,
  `Typ` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `ID_pracownika` int(10) NOT NULL,
  `ID_pacjenta` int(10) NOT NULL,
  `ID_gabinetu` int(10) NOT NULL,
  `Data_wizyty` date NOT NULL,
  `Godzina_wizyty` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `wizyta`
--

INSERT INTO `wizyta` VALUES(1, 'Badanie', 1, 1, 1, '2020-06-08', '10:00:00');
INSERT INTO `wizyta` VALUES(2, 'Badanie ', 1, 7, 3, '2020-06-10', '14:00:00');
INSERT INTO `wizyta` VALUES(3, 'Badanie', 3, 5, 1, '2020-06-11', '11:00:00');
INSERT INTO `wizyta` VALUES(4, 'Badanie', 6, 11, 2, '2020-06-15', '13:00:00');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `gabinet`
--
ALTER TABLE `gabinet`
  ADD PRIMARY KEY (`ID_gabinetu`),
  ADD KEY `ID_pracownika` (`ID_pracownika`);

--
-- Indeksy dla tabeli `lekarz`
--
ALTER TABLE `lekarz`
  ADD PRIMARY KEY (`ID_pracownika`);

--
-- Indeksy dla tabeli `pacjent`
--
ALTER TABLE `pacjent`
  ADD PRIMARY KEY (`ID_pacjenta`);

--
-- Indeksy dla tabeli `pracownik`
--
ALTER TABLE `pracownik`
  ADD PRIMARY KEY (`ID_pracownika`);

--
-- Indeksy dla tabeli `recepta`
--
ALTER TABLE `recepta`
  ADD PRIMARY KEY (`ID_recepty`),
  ADD KEY `ID_wizyty` (`ID_wizyty`);

--
-- Indeksy dla tabeli `uwagi`
--
ALTER TABLE `uwagi`
  ADD PRIMARY KEY (`ID_uwagi`),
  ADD KEY `ID_wizyty` (`ID_wizyty`);

--
-- Indeksy dla tabeli `wizyta`
--
ALTER TABLE `wizyta`
  ADD PRIMARY KEY (`ID_wizyty`),
  ADD KEY `ID_pacjenta` (`ID_pacjenta`),
  ADD KEY `ID_gabinetu` (`ID_gabinetu`),
  ADD KEY `ID_pracownika` (`ID_pracownika`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `pacjent`
--
ALTER TABLE `pacjent`
  MODIFY `ID_pacjenta` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `gabinet`
--
ALTER TABLE `gabinet`
  ADD CONSTRAINT `gabinet_ibfk_1` FOREIGN KEY (`ID_pracownika`) REFERENCES `lekarz` (`ID_pracownika`);

--
-- Ograniczenia dla tabeli `lekarz`
--
ALTER TABLE `lekarz`
  ADD CONSTRAINT `lekarz_ibfk_1` FOREIGN KEY (`ID_pracownika`) REFERENCES `pracownik` (`ID_pracownika`);

--
-- Ograniczenia dla tabeli `recepta`
--
ALTER TABLE `recepta`
  ADD CONSTRAINT `recepta_ibfk_1` FOREIGN KEY (`ID_wizyty`) REFERENCES `wizyta` (`ID_wizyty`);

--
-- Ograniczenia dla tabeli `uwagi`
--
ALTER TABLE `uwagi`
  ADD CONSTRAINT `uwagi_ibfk_1` FOREIGN KEY (`ID_wizyty`) REFERENCES `wizyta` (`ID_wizyty`);

--
-- Ograniczenia dla tabeli `wizyta`
--
ALTER TABLE `wizyta`
  ADD CONSTRAINT `wizyta_ibfk_1` FOREIGN KEY (`ID_pacjenta`) REFERENCES `pacjent` (`ID_pacjenta`),
  ADD CONSTRAINT `wizyta_ibfk_2` FOREIGN KEY (`ID_gabinetu`) REFERENCES `gabinet` (`ID_gabinetu`),
  ADD CONSTRAINT `wizyta_ibfk_3` FOREIGN KEY (`ID_pracownika`) REFERENCES `pracownik` (`ID_pracownika`);
COMMIT;

/* Uzytkownicy */

DROP USER IF EXISTS przychodniadb@localhost;
CREATE USER przychodniadb@localhost IDENTIFIED BY 'Zaq12wsx';
GRANT ALL PRIVILEGES ON przychodniadb.* TO przychodniadb@localhost;