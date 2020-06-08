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
