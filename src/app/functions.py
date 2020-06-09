import pymysql
import _datetime #nie działa


def connect():
    connection = pymysql.Connect(host='localhost',
                                 user='przychodniadb',
                                 password='Zaq12wsx',
                                 db='przychodniadb'
                                 # charset='uft8mb4',
                                 # cursorclass=pymysql.cursors.DictCursor
                                 )
    return connection


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
            print(result)
    finally:
        connection.close()
        return int(result[0])


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


def zarejestruj(typ, id_pracownika, id_pacjenta, id_gabinetu, data, godzina):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            id_wizyty = ID_wizyty()
            print(id_wizyty, typ, id_pracownika, id_pacjenta, id_gabinetu, data, godzina)
            sql = "INSERT INTO `wizyta` VALUES(%s, '%s', %s, %s, %s, '%s', '%s');" % (
                id_wizyty, typ, id_pracownika, id_pacjenta, id_gabinetu, data, godzina)
            print(sql)
            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


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
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()


def na_urlopie():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.Urlop " \
                  "FROM pracownik  INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika " \
                  "WHERE lekarz.Urlop = '1' " \
                  "ORDER BY Pracownik.Nazwisko ASC, Pracownik.Imie ASC;"

            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)

    finally:
        connection.close()


def dane_kontaktowe_lekarza(imie_lekarza, nazwisko_lekarza):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.Specjalizacja, pracownik.Telefon, pracownik.Mail " \
                  "FROM pracownik  INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika " \
                  "WHERE pracownik.Imie = '%s' AND pracownik.Nazwisko = '%s';" % (imie_lekarza, nazwisko_lekarza)
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)

    finally:
        connection.close()


def godziny_przyjec():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT pracownik.Imie, pracownik.Nazwisko, lekarz.ID_pracownika, gabinet.Godzina_rozpoczecia, gabinet.Godzina_zakonczenia " \
                  "FROM pracownik  INNER JOIN lekarz ON lekarz.ID_pracownika = pracownik.ID_pracownika  " \
                  "INNER JOIN gabinet ON gabinet.ID_pracownika = lekarz.ID_pracownika " \
                  "ORDER BY Pracownik.Nazwisko ASC, Pracownik.Imie ASC; "

            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)

    finally:
        connection.close()


def wizyty_lekarza_w_dniu(imie_lekarza, nazwisko_lekarza, dzien):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT pracownik.Imie, pracownik.Nazwisko, wizyta.Data_wizyty, wizyta.Godzina_wizyty " \
                  "FROM pracownik  INNER JOIN wizyta ON wizyta.ID_pracownika = pracownik.ID_pracownika " \
                  "WHERE pracownik.Imie = '%s' AND pracownik.Nazwisko = '%s' AND wizyta.Data_wizyty = '%s' " \
                  "ORDER BY wizyta.Godzina_wizyty ASC;" % (imie_lekarza, nazwisko_lekarza, dzien)

            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)

    finally:
        connection.close()
        #Trzeba poprawić aby wyświetlało dobrze godzinę


def wizyty_gabinet(nr_gabinetu):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT gabinet.Nr_gabinetu, gabinet.Pietro, wizyta.ID_wizyty, pacjent.Imie, pacjent.Nazwisko " \
                  "FROM gabinet  " \
                  "LEFT JOIN wizyta ON wizyta.ID_gabinetu = gabinet.ID_gabinetu  " \
                  "LEFT JOIN pacjent ON wizyta.ID_pacjenta = pacjent.ID_pacjenta WHERE gabinet.Nr_gabinetu = '%s';" % (nr_gabinetu)

            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)

    finally:
        connection.close()