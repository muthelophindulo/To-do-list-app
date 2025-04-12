import sqlite3 
def view():
    con = sqlite3.connect('test.db')

    cur = con.cursor()

    pulled_data = cur.execute('''SELECT * FROM item''')

    for data in pulled_data:
        print(data)

    con.close()
