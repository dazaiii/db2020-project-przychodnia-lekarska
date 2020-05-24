from typing import Optional, Any

import pymysql

print('Hello')

connection = pymysql.Connect(host='localhost',
                             user='przychodniadb',
                             password='Zaq12wsx',
                             db='przychodniadb'
                             #charset='uft8mb4',
                             #cursorclass=pymysql.cursors.DictCursor
                             )
print('Hello')
try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Pacjent"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)



finally:
    connection.close()
