-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 07 Cze 2020, 16:45
-- Wersja serwera: 10.4.11-MariaDB
-- Wersja PHP: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `przychodnia`
--
CREATE DATABASE IF NOT EXISTS `przychodniadb` DEFAULT CHARACTER SET utf8 COLLATE utf8_polish_ci;
USE `przychodnia`;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `gabinet`
--

CREATE TABLE `gabinet` (
  `ID_gabinetu` int(10) NOT NULL,
  `Nr_gabinetu` int(10) NOT NULL,
  `Godzina_rozpoczecia` time NOT NULL,
  `Godzina_zakonczenia` time NOT NULL,
  `ID_pracownika` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `lekarz`
--

CREATE TABLE `lekarz` (
  `ID_pracownika` int(10) NOT NULL,
  `Specjalizacja` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Staz_pracy` int(10) NOT NULL,
  `Etat` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Urlop` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pacjent`
--

CREATE TABLE `pacjent` (
  `ID_pacjenta` int(10) NOT NULL,
  `Imie` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Nazwisko` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Data_urodzenia` date NOT NULL,
  `Pesel` int(10) NOT NULL,
  `Miejsce_zamieszkania` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Telefon` int(10) NOT NULL,
  `Mail` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Ubezpieczenie` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pracownik`
--

CREATE TABLE `pracownik` (
  `ID_pracownika` int(11) NOT NULL,
  `Imie` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Nazwisko` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Data_urodzenia` date NOT NULL,
  `Pesel` int(10) NOT NULL,
  `Miejsce_zamieszkania` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Telefon` int(10) NOT NULL,
  `Mail` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `Funkcja` varchar(50) COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

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
-- Indeksy dla tabeli `uwagi`
--
ALTER TABLE `uwagi`
  ADD PRIMARY KEY (`ID_uwagi`);

--
-- Indeksy dla tabeli `wizyta`
--
ALTER TABLE `wizyta`
  ADD PRIMARY KEY (`ID_wizyty`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
