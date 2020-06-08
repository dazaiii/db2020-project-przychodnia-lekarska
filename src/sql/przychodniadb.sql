SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


--
-- Baza danych: `przychodniadb`
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
  `ID_pracownika` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `gabinet`
--

INSERT INTO `gabinet` (`ID_gabinetu`, `Nr_gabinetu`, `Pietro`, `Godzina_rozpoczecia`, `Godzina_zakonczenia`, `ID_pracownika`) VALUES
(1, 10, 1, '08:00:00', '16:00:00', 1),
(2, 11, 1, '09:30:00', '17:30:00', 2),
(3, 20, 2, '08:30:00', '16:00:00', 3),
(4, 21, 2, '08:00:00', '14:00:00', 4),
(5, 13, 1, '08:00:00', '15:00:00', 8),
(6, 32, 3, '09:00:00', '15:00:00', 0),
(7, 12, 1, '08:00:00', '16:00:00', 0),
(8, 14, 1, '08:30:00', '16:30:00', 9),
(9, 15, 1, '08:00:00', '16:30:00', 10),
(10, 22, 2, '09:00:00', '15:00:00', 11),

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

INSERT INTO `lekarz` (`ID_pracownika`, `Specjalizacja`, `Staz_pracy`, `Etat`, `Urlop`) VALUES
(1, 'Kardiolog', 1, 'staz', 0),
(2, 'Dermatolog', 10, 'pełny', 0),
(3, 'Pediatra', 12, 'pełny', 1),
(4, 'Neurolog', 5, 'pełny', 0),
(8, 'Ogolny', 15, 'pelny', 0),
(9, 'Kardiolog', 10, 'pełny', 0),
(10, 'Okulista', 1, 'staż', 0),
(11, 'Okulista', 20, 'pełny', 1),


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

INSERT INTO `pacjent` (`ID_pacjenta`, `Imie`, `Nazwisko`, `Data_urodzenia`, `Pesel`, `Miejsce_zamieszkania`, `Telefon`, `Mail`, `Ubezpieczenie`) VALUES
(1, 'Adam', 'Nowak', '1920-02-11', '20021112345', 'Kraków', 123456789, 'an@mail.com', 0),
(2, 'Janusz', 'Kowalski', '1960-05-11', '60051112345', 'Kraków', 123456789, 'jk@mail.com', 1),
(3, 'Maciej', 'Glowczyk', '1981-04-12', '81041212345', 'Tarnów', 346283716, 'maciej_glowczyk@mail.com', 1),
(4, 'Krzysztof', 'Rabczewski', '1969-02-05', '69020538261', 'Oświęcim', 609752817, 'k_rabczewski@mail.com', 1),
(5, 'Krzysztof', 'Nowakowski', '1978-11-05', '78110509675', 'Kraków', 890765876, 'k_nowakowski@mail.com', 1),
(6, 'Mikolaj', 'Mikolajowski', '1990-12-11', '90121178256', 'Kraków', 214748364, 'mikolajowski@mail.com', 1),
(7, 'Mariusz', 'Budzyn', '1929-01-01', '21010176543', 'Niepołomice', 789654321, 'budzyn@mail.com', 1),
(8, 'Justyna', 'Kowal', '1978-02-05', '80205127651', 'Kraków', 147483647, 'justyna_kowal@mail.com', 1),
(9, 'Zofia', 'Piotrowska', '2001-10-10', '01101076578', 'Niepołomice', 789654678, 'piotrowksa@mail.com', 1),
(10, 'Joanna', 'Maciszewska', '1998-12-10', '98121076238', 'Wieliczka', 654789678, 'maciszewska@mail.com', 0),
(11, 'Zygmunt', 'Wolak', '1950-04-27', '50042789765', 'Kraków', 654789654, 'zygmunt_wolak@mail.com', 1),
(12, 'Katarzyna', 'Szymańska', '1970-01-01', '70010105209', 'Bochnia', 768954765, 'szymanska@mail.com', 1),
(13, 'Zofia', 'Kwiatkowska', '1981-02-02', '81020245671', 'Brzesko', 567829384, 'kwi@mail.com', 1),
(14, 'Grzegorz', 'Piotrowski', '1976-11-27', '76112134213', 'Brzesko', 789321453, 'piotrowski.g@mail.com', 1),
(15, 'Wojciech', 'Jabłoński', '1990-05-11', '90051109465', 'Kraków', 876456765, 'jablonek@mail.com', 1),

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

INSERT INTO `pracownik` (`ID_pracownika`, `Imie`, `Nazwisko`, `Data_urodzenia`, `Pesel`, `Miejsce_zamieszkania`, `Telefon`, `Mail`, `Funkcja`) VALUES
(1, 'Piotr', 'Majewski', '1940-02-11', '40021167854', 'Kraków', 123456789, 'majewski@mail.com', 'Lekarz'),
(2, 'Krzysztof', 'Jarczewski', '1959-02-11', '59021112345', 'Kraków', 456787658, 'kj@mail.com', 'Lekarz'),
(3, 'Karolina', 'Malinowska', '1967-04-04', '67040454678', 'Oświęcim', 567865456, 'malinowska@mail.com', 'Lekarz'),
(4, 'Malwina', 'Janiszewska', '1987-05-20', '87052087659', 'Kraków', 567876908, 'janiszewska@mail.com', 'Lekarz'),
(5, 'Janina', 'Wojtaszewska', '1969-03-15', '69031512345', 'Wieliczka', 123456789, 'wojtaszewska@mail.com', 'Pielegniarka'),
(6, 'Edyta', 'Wojcik', '1970-05-15', '70051512345', 'Tarnów', 123456789, 'edyta_wojcik@mail.com', 'Pielegniarka'),
(7, 'Julia', 'Kowalewska', '1971-10-15', '71101512328', 'Kraków', 567387659, 'kowalewska_julia@mail.com', 'Recepcjonistka'),
(8, 'Marian', 'Gorski', '1988-08-22', '87052288659', 'Kraków', 567876908, 'mgorski@mail.com', 'Lekarz'),
(9, 'Zbigniew', 'Janik', '1960-02-15', '60021567845', 'Kraków', 873948273, 'janik_zbigniew@mail.com', 'Lekarz'),
(10, 'Tomasz', 'Andrzejewski', '1984-07-07', '84070790531', 'Kraków', 647583928, 'andrzejewski@mail.com', 'Lekarz'),
(11, 'Maria', 'Zięba', '1965-04-16', '65041529035', 'Tuchów', 837491876, 'ziebamaria@mail.com', 'Lekarz'),


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

INSERT INTO `recepta` (`ID_recepty`, `Nazwa_lekarstwa`, `Sposob_podania`, `ID_wizyty`) VALUES
(1, 'Ibuprom', 'Doustnie', 1),
(2, 'Ibupm', 'Doustnie', 2),
(3, 'Nurofen', 'Doustnie', 3),
(5, 'Anpan', 'Doustnie', 4),
(6, 'Fenistil', 'Maść', 6),
(7, 'Dermedix', 'Żel', 8),
(8, 'Altacet', 'Maść', 12),

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `skierowanie`
--

CREATE TABLE `skierowanie` (
  `ID_skierowania` int(10) NOT NULL,
  `ID_wizyty` int(10) NOT NULL,
  `Typ` varchar(50) COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `skierowanie`
--

INSERT INTO `skierowanie` (`ID_skierowania`, `ID_wizyty`, `Typ`) VALUES
(1, 1, 'Do kardiologa'),
(2, 2, 'Do dermatologa'),
(3, 3, 'Do kardiologa'),
(4, 4, 'Na szczepienie'),


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

INSERT INTO `wizyta` (`ID_wizyty`, `Typ`, `ID_pracownika`, `ID_pacjenta`, `ID_gabinetu`, `Data_wizyty`, `Godzina_wizyty`) VALUES
(1, 'Badanie', 1, 1, 1, '2020-06-08', '10:00:00'),
(2, 'Badanie ', 1, 7, 3, '2020-06-10', '14:00:00'),

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `gabinet`
--
ALTER TABLE `gabinet`
  ADD PRIMARY KEY (`ID_gabinetu`);

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
  ADD PRIMARY KEY (`ID_recepty`);

--
-- Indeksy dla tabeli `skierowanie`
--
ALTER TABLE `skierowanie`
  ADD PRIMARY KEY (`ID_skierowania`),
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
  MODIFY `ID_pacjenta` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `lekarz`
--
ALTER TABLE `lekarz`
  ADD CONSTRAINT `lekarz_ibfk_1` FOREIGN KEY (`ID_pracownika`) REFERENCES `pracownik` (`ID_pracownika`);

--
-- Ograniczenia dla tabeli `skierowanie`
--
ALTER TABLE `skierowanie`
  ADD CONSTRAINT `skierowanie_ibfk_1` FOREIGN KEY (`ID_wizyty`) REFERENCES `wizyta` (`ID_wizyty`);

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
