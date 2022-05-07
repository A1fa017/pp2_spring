import psycopg2
from config import database, host, user, password

connection = psycopg2.connect(
    host=host, 
    database=database,
    user=user,
    password=password
)

table = connection.cursor()

answer = input("You want to delete by name or phone? ")

if answer == 'name':
    delete = input('what user you want to delete?: ')
    table.execute(f"DELETE FROM phonebook1 WHERE user_name = '{delete}'")
elif answer == 'phone':
    delete = input('what phone you want to delete?: ')
    table.execute(f"DELETE FROM phonebook1 WHERE user_number = '{delete}'")


connection.commit()
table.close()
connection.close()