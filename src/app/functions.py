import pymysql


def connect():
    connection = pymysql.Connect(host='localhost',
                                 user='przychodniadb',
                                 password='Zaq12wsx',
                                 db='przychodniadb'
                                 # charset='uft8mb4',
                                 # cursorclass=pymysql.cursors.DictCursor
                                 )
    return connection


#1.1
def recepta(imie, nazwisko):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `pacjent`.`Imie`, `pacjent`.`Nazwisko`, `wizyta`.`ID_pacjenta`, " \
                  "`recepta`.`Nazwa_lekarstwa`, `recepta`.`Sposob_podania` " \
                  "FROM `pacjent`  LEFT JOIN `wizyta` ON `wizyta`.`ID_pacjenta` = `pacjent`.`ID_pacjenta`  " \
                  "LEFT JOIN `recepta` ON `recepta`.`ID_wizyty` = `wizyta`.`ID_wizyty` " \
                  "WHERE `pacjent`.`Imie` = '%s' AND `pacjent`.`Nazwisko` = '%s'" % (imie, nazwisko)

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1], row[2], row[3], row[4])
    finally:
        connection.close()



#1.2
def na_urlopie(wybor):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.Urlop " \
                  "FROM pracownik  INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika " \
                  "WHERE lekarz.Urlop = '%s' " \
                  "ORDER BY Pracownik.Nazwisko ASC, Pracownik.Imie ASC;" % (wybor)

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1], row[2])

    finally:
        connection.close()


#1.3 dane kontaktowe wielu osób
def dane_kontaktowe(tabela):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT Imie, Nazwisko, Telefon, Mail " \
                  "FROM %s "  % (tabela)

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1], row[2], row[3])

    finally:
        connection.close()


#1.3 dane kontaktowe jednej osoby
def dane_kontaktowe_1(tabela,imie, nazwisko):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT Imie, Nazwisko, Telefon, Mail " \
                  "FROM %s " \
                  "WHERE Imie = '%s' AND Nazwisko = '%s';" % (tabela, imie, nazwisko)

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1], row[2], row[3])

    finally:
        connection.close()



#1.4
def godziny_przyjec():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.ID_pracownika, gabinet.Godzina_rozpoczecia, gabinet.Godzina_zakonczenia " \
                  "FROM pracownik  INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika  " \
                  "INNER JOIN gabinet ON gabinet.ID_pracownika = lekarz.ID_pracownika " \
                  "ORDER BY Pracownik.Nazwisko ASC, Pracownik.Imie ASC; "

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1], row[2], row[3], row[4])

    finally:
        connection.close()



#1.4
def godziny_przyjec_lekarza(imie_lekarza, nazwisko_lekarza):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.Specjalizacja, gabinet.Nr_gabinetu, gabinet.Pietro, gabinet.Godzina_rozpoczecia, gabinet.Godzina_zakonczenia " \
                  "FROM pracownik  INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika " \
                  "INNER JOIN gabinet ON gabinet.ID_pracownika = lekarz.ID_pracownika " \
                  "WHERE pracownik.Imie = '%s' AND pracownik.Nazwisko = '%s';" % (imie_lekarza, nazwisko_lekarza)

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

    finally:
        connection.close()


#1.5
def wyswietl_wizyty():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT pracownik.Imie, pracownik.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty, gabinet.Nr_gabinetu " \
                  "FROM pracownik  INNER JOIN wizyta ON wizyta.ID_pracownika = pracownik.ID_pracownika  " \
                  "INNER JOIN gabinet ON wizyta.ID_gabinetu = gabinet.ID_gabinetu " \
                  "ORDER BY wizyta.data_wizyty ASC, wizyta.godzina_wizyty ASC;"

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1], row[2], row[3])

    finally:
        connection.close()


#1.5
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


#1.5
def wizyty_gabinet(nr_gabinetu):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT gabinet.Nr_gabinetu, gabinet.Pietro, wizyta.ID_wizyty, pacjent.Imie, pacjent.Nazwisko " \
                  "FROM gabinet  " \
                  "LEFT JOIN wizyta ON wizyta.ID_gabinetu = gabinet.ID_gabinetu  " \
                  "LEFT JOIN pacjent ON wizyta.ID_pacjenta = pacjent.ID_pacjenta WHERE gabinet.Nr_gabinetu = '%s';" % (nr_gabinetu)

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1], row[2], row[3],row[4])

    finally:
        connection.close()


#1.5
def ilosc_wizyt(data1, data2):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT Data_wizyty, COUNT(Data_wizyty) AS ‘Ilość’ FROM wizyta  " \
                  "WHERE Data_wizyty BETWEEN '%s' AND '%s' " \
                  "GROUP BY Data_wizyty ORDER BY Data_wizyty ASC;" % (data1, data2)
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1])

    finally:
        connection.close()


#1.5
def ilosc_wizyt_miesiac(data):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT Data_wizyty, COUNT(Data_wizyty) AS ‘Ilość’ FROM wizyta  " \
                  "WHERE Data_wizyty LIKE '%s%s'" \
                  "GROUP BY Data_wizyty ORDER BY Data_wizyty ASC;" % (data,'%')
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1])

    finally:
        connection.close()


#1.6
def historia_wizyt(imie,nazwisko):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT pacjent.Imie, pacjent.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty FROM pacjent  " \
                  "INNER JOIN wizyta ON wizyta.ID_pacjenta = pacjent.ID_pacjenta " \
                  "WHERE pacjent.Imie = '%s' AND pacjent.Nazwisko = '%s' " \
                  "ORDER BY Wizyta.Data_wizyty ASC, Wizyta.Godzina_wizyty ASC;" % (imie,nazwisko)

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0],row[1],row[2],row[3])
    finally:
        connection.close()

#1.6
def historia_wizyt_przedzial(imie, nazwisko, dzien1, dzien2):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT pacjent.Imie, pacjent.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty FROM pacjent  " \
                  "INNER JOIN wizyta ON wizyta.ID_pacjenta = pacjent.ID_pacjenta " \
                  "WHERE pacjent.Imie = '%s' AND pacjent.Nazwisko = '%s' AND Data_wizyty BETWEEN '%s' AND '%s'" \
                  "ORDER BY Wizyta.Data_wizyty ASC, Wizyta.Godzina_wizyty ASC;" % (imie,nazwisko,dzien1,dzien2)

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1], row[2], row[3])

    finally:
        connection.close()


#1.7
def wyszukaj_skierowania(imie_pacjenta, nazwisko_pacjenta):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT pacjent.Imie, pacjent.Nazwisko, wizyta.ID_pacjenta, skierowanie.ID_skierowania, skierowanie.Typ " \
                  "FROM pacjent " \
                  "INNER JOIN wizyta ON wizyta.ID_pacjenta = pacjent.ID_pacjenta  " \
                  "INNER JOIN skierowanie ON skierowanie.ID_wizyty = wizyta.ID_wizyty " \
                  "WHERE pacjent.Imie = '%s' AND pacjent.Nazwisko = '%s';" % (imie_pacjenta, nazwisko_pacjenta)

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1], row[2], row[3], row[4])

    finally:
        connection.close()


#1.8
def szczepienia():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT wizyta.Typ, pacjent.Imie, pacjent.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty, gabinet.Nr_gabinetu " \
                  "FROM wizyta  " \
                  "INNER JOIN pacjent ON wizyta.ID_pacjenta = pacjent.ID_pacjenta  " \
                  "INNER JOIN gabinet ON wizyta.ID_gabinetu = gabinet.ID_gabinetu " \
                  "WHERE wizyta.Typ = 'szczepienie' " \
                  "ORDER BY Wizyta.Data_wizyty ASC, Wizyta.Godzina_wizyty ASC;"

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1], row[2], row[3],row[4], row[5])

    finally:
        connection.close()

#1.8
def szczepienia_pacjenta(imie_pacjenta, nazwisko_pacjenta):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT wizyta.Typ, pacjent.Imie, pacjent.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty, gabinet.Nr_gabinetu " \
                  "FROM wizyta  " \
                  "INNER JOIN pacjent ON wizyta.ID_pacjenta = pacjent.ID_pacjenta  " \
                  "INNER JOIN gabinet ON wizyta.ID_gabinetu = gabinet.ID_gabinetu " \
                  "WHERE wizyta.Typ = 'szczepienie' AND pacjent.Imie = '%s' AND pacjent.Nazwisko = '%s' " \
                  "ORDER BY Wizyta.Data_wizyty ASC, Wizyta.Godzina_wizyty ASC;" % (imie_pacjenta, nazwisko_pacjenta)

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1], row[2], row[3], row[4], row[5])

    finally:
        connection.close()

#1.9
def lekarze_etat(nazwa):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.Etat FROM pracownik  " \
                  "INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika WHERE lekarz.Etat = '%s'; " % (nazwa)

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1], row[2])

    finally:
        connection.close()


#1.10
def wyswietl_wszystkich():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT Imie, Nazwisko, Data_urodzenia " \
                  "FROM Pacjent " \
                  "UNION SELECT Imie, Nazwisko, Data_urodzenia " \
                  "FROM Pracownik " \
                  "ORDER BY Data_urodzenia;"

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1], row[2])

    finally:
        connection.close()


#1.11
def wyszukaj_pesel(imie_pacjenta, nazwisko_pacjenta):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT pacjent.Imie, pacjent.Nazwisko, pacjent.Data_urodzenia, pacjent.Pesel " \
                  "FROM pacjent " \
                  "WHERE pacjent.Imie = '%s' AND pacjent.Nazwisko = '%s';" % (imie_pacjenta, nazwisko_pacjenta)

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1], row[2], row[3])

    finally:
        connection.close()


#1.12
def grupuj_zawodem():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT Pracownik.Funkcja AS 'Zawod pracownika', " \
                  "COUNT(Pracownik.funkcja) AS 'Ilosc pracownikow' " \
                  "FROM Pracownik " \
                  "GROUP BY Pracownik.Funkcja " \
                  "ORDER BY Pracownik.Funkcja ASC;"

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1])

    finally:
        connection.close()

#1.13
def zlicz_lekarzy():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT Lekarz.Specjalizacja, COUNT(Lekarz.Specjalizacja) AS 'Ilość' " \
                  "FROM Lekarz " \
                  "GROUP BY Lekarz.Specjalizacja " \
                  "ORDER BY Lekarz.Specjalizacja ASC;"

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1])

    finally:
        connection.close()

#1.13
def zlicz_lekarzy_specjalizacji(specjalizacja):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT Lekarz.Specjalizacja, COUNT(Lekarz.Specjalizacja) AS 'Ilość' " \
                  "FROM Lekarz " \
                  "WHERE Lekarz.Specjalizacja = '%s'" \
                  "GROUP BY Lekarz.Specjalizacja;" % (specjalizacja)

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0], row[1])

    finally:
        connection.close()

#2.1
def ubezpieczenie(imie, nazwisko):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT ubezpieczenie , ID_pacjenta FROM Pacjent WHERE Imie='%s' AND Nazwisko='%s'" % (imie, nazwisko)
            cursor.execute(sql)
            result = cursor.fetchone()
            # print(result)
    finally:
        connection.close()
        return result  # result[0] zwraca informację czy pacjent ma ubezpieczenie, result[1] ID_pacjenta



#2.1
def urlop(imie_lekarza, nazwisko_lekarza):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `lekarz`.`Urlop`, `gabinet`.`ID_pracownika`, `gabinet`.`ID_gabinetu` FROM `pracownik` " \
                  "INNER JOIN `lekarz` ON `lekarz`.`ID_pracownika` = `pracownik`.`ID_pracownika`" \
                  "INNER JOIN `gabinet` ON `gabinet`.`ID_pracownika` = `lekarz`.`ID_pracownika`" \
                  "WHERE `pracownik`.`Imie` = '%s' AND `pracownik`.`Nazwisko` = '%s';" % (
                      imie_lekarza, nazwisko_lekarza)

            cursor.execute(sql)
            result = cursor.fetchone()
            # print(result)
    finally:
        connection.close()
        return result  # result[0] oznacza czy lekarz jest na urlopie, result[1] to jego ID, result[2] ID_gabinetu w którym przyjmuje



#2.1
def dostepnosc_gabinetu(id_pracownika, godzina, data):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT COUNT(`wizyta`.`ID_pracownika`) FROM `wizyta`" \
                  "WHERE `wizyta`.`ID_pracownika` = '%s' AND `wizyta`.`Godzina_wizyty` = '%s' AND " \
                  "`wizyta`.`Data_wizyty` = '%s';" \
                  % (id_pracownika, godzina, data)

            cursor.execute(sql)
            result = cursor.fetchone()
            #print(result)
    finally:
        connection.close()
        return int(result[0])



#2.1
def ID_wizyty():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT COUNT(ID_wizyty) FROM Wizyta;"
            cursor.execute(sql)
            result = cursor.fetchone()
            id_wizyty = int(result[0]) + 1
    finally:
        connection.close()
        return id_wizyty



#2.1
def zarejestruj(typ, id_pracownika, id_pacjenta, id_gabinetu, data, godzina):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            id_wizyty = ID_wizyty()
            print(id_wizyty, typ, id_pracownika, id_pacjenta, id_gabinetu, data, godzina)
            sql = "INSERT INTO `wizyta` VALUES(%s, '%s', %s, %s, %s, '%s', '%s');" % (
                id_wizyty, typ, id_pracownika, id_pacjenta, id_gabinetu, data, godzina)
            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


#2.2
def id_osoby(tabela):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT COUNT(*) FROM %s;" % (tabela)
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            id_os = int(result[0]) + 1
    finally:
        connection.close()
        return id_os


#2.2
def dodaj_pacjenta(id_pacjenta,imie, nazwisko, data_urodzenia, pesel, miejsce_zamieszkania, telefon, mail,ubezpieczenie):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `pacjent` (`ID_pacjenta`, `Imie`, `Nazwisko`, `Data_urodzenia`, `Pesel`, `Miejsce_zamieszkania`, " \
                  "`Telefon`, `Mail`, `Ubezpieczenie`) VALUES(%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                id_pacjenta,imie, nazwisko, data_urodzenia, pesel, miejsce_zamieszkania, telefon, mail,ubezpieczenie)

            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


#2.2
def dodaj_pracownika(id_pracownika,imie,nazwisko,data_urodzenia,pesel,miejsce_zamieszkania,telefon,mail,funkcja):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `pracownik` (`ID_pracownika`, `Imie`, `Nazwisko`, `Data_urodzenia`, `Pesel`, " \
                  "`Miejsce_zamieszkania`, `Telefon`, `Mail`, `Funkcja`) " \
                  "VALUES (%s, '%s', '%s', '%s', '%s', '%s', %s, '%s', '%s')" % (
                id_pracownika,imie,nazwisko,data_urodzenia,pesel,miejsce_zamieszkania,telefon,mail,funkcja)

            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


#2.2
def dodaj_lekarza(id_pracownika,specjalizacja,staz,etat):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `lekarz` (`ID_pracownika`, `Specjalizacja`, `Staz_pracy`, `Etat`, `Urlop`)" \
                  " VALUES(%s, '%s', %s, '%s', 0);" % (id_pracownika,specjalizacja,staz,etat)

            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()

#2.3
def modyfikuj_dane_kontaktowe(tabela,imie,nazwisko,kolumna,dane):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE %s SET %s = '%s' WHERE Imie = '%s' AND Nazwisko = '%s'" % (tabela, kolumna, dane, imie, nazwisko)

            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


#2.4
def usun_wizyte(imie,nazwisko,data,godzina):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT ID_wizyty FROM wizyta WHERE id_pacjenta = (SELECT ID_pacjenta FROM pacjent WHERE Imie = '%s' " \
                  "AND Nazwisko = '%s') AND Data_wizyty = '%s' AND Godzina_wizyty = '%s';" % (imie, nazwisko,data,godzina)
            cursor.execute(sql)
            id_wizyty = cursor.fetchone()
            id_wizyty = int(id_wizyty[0])

            sql = "DELETE FROM Skierowanie WHERE ID_wizyty = '%s'" % (id_wizyty)
            cursor.execute(sql)
            sql = "DELETE FROM Recepta WHERE ID_wizyty = '%s'" % (id_wizyty)
            cursor.execute(sql)
            sql = "DELETE FROM Wizyta WHERE ID_wizyty = '%s'" % (id_wizyty)
            cursor.execute(sql)

            connection.commit()

    finally:
        connection.close()


#2.5
def wpisz_urlop(imie,nazwisko):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE Lekarz SET Lekarz.urlop = 1 WHERE (SELECT ID_pracownika from Pracownik WHERE Pracownik.Imie " \
                  "= '%s' AND Pracownik.Nazwisko = '%s') = ID_pracownika;" % (imie,nazwisko)
            cursor.execute(sql)
            connection.commit()

    finally:
        connection.close()

#2.6
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

            sql = "INSERT INTO `skierowanie` (`ID_skierowania`, `ID_wizyty`, `Typ`)" \
              "VALUES(%s, %s, '%s');" % (id_skierowania, id_wizyty, do_kogo)
            cursor.execute(sql)
            connection.commit()

    finally:
        connection.close()



#2.7
def dodaj_recepte(imie, nazwisko, data, godzina):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT ID_wizyty FROM wizyta WHERE id_pacjenta = (SELECT ID_pacjenta FROM pacjent WHERE Imie = '%s' " \
                  "AND Nazwisko = '%s') AND Data_wizyty = '%s' AND Godzina_wizyty = '%s';" % (
                  imie, nazwisko, data, godzina)
            cursor.execute(sql)
            id_wizyty = cursor.fetchone()
            id_wizyty = int(id_wizyty[0])

            sql = "SELECT COUNT(*) FROM Recepta;"
            cursor.execute(sql)
            id_recepty = cursor.fetchone()
            id_recepty = int(id_recepty[0]) + 1
            print(id_recepty)

            lekarstwo = input('Podaj jakie lekarstwo przepisać: ')
            sposob_uzycia = input('Podaj sposób użycia leku: ')

            sql = "INSERT INTO `recepta` (`ID_recepty`, `Nazwa_lekarstwa`, `Sposob_podania`, `ID_wizyty`)" \
                  "VALUES(%s, '%s', '%s', %s);" % (id_recepty, lekarstwo, sposob_uzycia, id_wizyty)
            cursor.execute(sql)
            connection.commit()

    finally:
        connection.close()


#2.8
def zmien_ubezpieczenie(imie,nazwisko):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT Ubezpieczenie FROM Pacjent WHERE Imie = '%s' AND Nazwisko = '%s'" % (imie, nazwisko)
            cursor.execute(sql)
            ubezpieczenie = cursor.fetchone()
            ubezpieczenie = int(ubezpieczenie[0])

            if ubezpieczenie == 0:
                sql = "UPDATE Pacjent SET Ubezpieczenie = 1 WHERE Imie = '%s' AND Nazwisko = '%s'" % (imie, nazwisko)
            else:
                sql = "UPDATE Pacjent SET Ubezpieczenie = 0 WHERE Imie = '%s' AND Nazwisko = '%s'" % (imie, nazwisko)

            cursor.execute(sql)
            connection.commit()

    finally:
        connection.close()
