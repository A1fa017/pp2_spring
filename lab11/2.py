import psycopg2
from config import host, database, user, password

def insert(connection,name,phone):
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO PhoneBook
            VALUES(%s,%s,%s)""",
            (name,phone)
        )

def update(conection,name,phone):
    with connection.cursor() as cursor:
        cursor.execute(
            """UPDATE PhoneBook
            SET user_phone = %s
            WHERE user_name = %s""",
            (phone,name)
        )

try:
    connection = psycopg2.connect(
        database = database,
        user = user,
        host = host,
        password = password
    )
    connection.autocommit = True
    
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT * FROM PhoneBook"""
        )
        select = cursor.fetchall()

    name = input()
    phone = input()

    cnt = 0
    for sub in select:
        if name in sub:
            cnt += 1
    if cnt == 0:
        insert(connection, name, phone)
    else:
        update(connection,name,phone)

except Exception as ex:
    print(ex)

finally:
    if connection:
        connection.close()
        print('conection is closed')