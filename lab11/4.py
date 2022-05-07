import psycopg2
from config import database, host, user, password
connection = psycopg2.connect(
    host=host, 
    database=database,
    user=user,
    password=password
)
beginning = input()
ending = input()
table = connection.cursor()
def dates_by_limit(beginning, ending):
    try:
        table.callproc('querying_by_limit', (beginning, ending))
        myresult = table.fetchall()
        for i in myresult:
            print(i)
        table.commit()
    except Exception as e:
        print(str(e))
    finally:
        table.close()
dates_by_limit()