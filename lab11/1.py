import psycopg2
from config import host, database, user, password

connection = psycopg2.connect(
    host=host, 
    database=database,
    user=user,
    password=password
)

table = connection.cursor()
def outputalldata():
    table.execute("SELECT user_name,user_phone from phonebook1")
    myresult = table.fetchall()
    print('      |')
    print("NAME  |  PHONE")
    print('------------------------------')

    for i in myresult:
        print(i[0],' | ',i[1])
outputalldata()