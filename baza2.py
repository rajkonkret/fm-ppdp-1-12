import sqlite3

sql_connection = None
try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    query = '''
    CREATE TABLE IF NOT EXISTS SqliteDB (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    '''

    with open('tables.sql', 'r') as file:
        sql_script = file.read()

    cursor = sql_connection.cursor()
    print("Baza danych podłączona")
    # 
    # cursor.execute(query)
    # sql_connection.commit()
    cursor.executescript(sql_script)

except sqlite3.Error as e:
    print("Bład podczas otwierania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")
