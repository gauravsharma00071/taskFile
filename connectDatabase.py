import pyodbc
import schedule
import time
"""
In this complete function firstly i use pyodbc to connection with database then add
all its credetials which are used for connection both of them .
here a another function for inserting value also defined , we can give a query for this 
after that i also make a another time schedule expression for insert values after 1 hour automatically
this function will call
DocString By
Gaurav Sharma

"""
def connect_to_db():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'  
        'DATABASE=task;'  
        'UID=root;'  
        'PWD=Root@123;'
    )
    return conn


def insert_data():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        sql = """INSERT INTO table_Name (Name, class, rollNo) 
                 VALUES (?, ?, ?)"""

        data = ('value1', 'value2', 'value3')

        cursor.execute(sql, data)
        conn.commit()

        print(f"Data inserted successfully at {time.strftime('%Y-%m-%d %H:%M:%S')}")

    except pyodbc.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()


schedule.every(1).hours.do(insert_data)

while True:
    schedule.run_pending()
    time.sleep(1)
