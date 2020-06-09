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



#1
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



#1
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



#1
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



#1
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



#1
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



#2
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



#3
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


#4 dane kontaktowe wielu osób
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


#4 dane kontaktowe jednej osoby
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



#5
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



#5
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




#6
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


#6
def dodaj_pacjenta(id_pacjenta,imie, nazwisko, data_urodzenia, pesel, miejsce_zamieszkania, telefon, mail,ubezpieczenie):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `pacjent` (`ID_pacjenta`, `Imie`, `Nazwisko`, `Data_urodzenia`, `Pesel`, `Miejsce_zamieszkania`, `Telefon`, `Mail`, `Ubezpieczenie`) VALUES(%s, '%s', '%s', '%s', '%s', '%s', %s, '%s', %s)," % (
                id_pacjenta,imie, nazwisko, data_urodzenia, pesel, miejsce_zamieszkania, telefon, mail,ubezpieczenie)

            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


#6
def dodaj_pracownika(id_pracownika,imie,nazwisko,data_urodzenia,pesel,miejsce_zamieszkania,telefon,mail,funkcja):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `pracownik` (`ID_pracownika`, `Imie`, `Nazwisko`, `Data_urodzenia`, `Pesel`, " \
                  "`Miejsce_zamieszkania`, `Telefon`, `Mail`, `Funkcja`) " \
                  "VALUES (%dsS, '%s', '%s', '%s', '%s', '%s', %s, '%s', '%s')," % (
                id_pracownika,imie,nazwisko,data_urodzenia,pesel,miejsce_zamieszkania,telefon,mail,funkcja)

            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()
