import psycopg2
from config import database, host, user, password

connection = psycopg2.connect(
    host=host, 
    database=database,
    user=user,
    password=password
)

table = connection.cursor()

# data = [('almas','87052223456'),
# ('damir','87073999206'),
# ('baxa','87054442846'),
# ('dama','21312'),
# ('tileuhan','dasdad')]

data = {
    'almas':'87052223456',
    'damir':'87073999206',
    'baxa':'87054442846',
    'dama':'21312',
    'tileuhan':'dasdad',
    '123123':'asdadas'

}

incorrect = []

def sort(data):
    for key,value in data.items():
        if key.isalpha() == False:
            incorrect.append((key,value))
            continue
        if value.isdigit() == False:
            incorrect.append((key,value))
            continue
        if len(value)!=11:
            incorrect.append((key,value))
            continue
        table.execute("INSERT INTO phonebook1 VALUES (%s,%s)",(key,value))
        connection.commit()
sort(data)
print(incorrect)