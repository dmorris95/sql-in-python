import mysql.connector
from mysql.connector import Error

#Task 1: SQL Between Use
def get_members_in_age_range(start_age, end_age):
    between_statement = "SELECT name, age, trainer_id FROM Members WHERE age between %s AND %s"
    between_vars = start_age, end_age
    cursor.execute(between_statement, between_vars)
    result = cursor.fetchall()
    for row in result:
        print(row)


try: 
    gymdb = mysql.connector.connect(
        database = "gym_db",
        host="your_host",
        user="root",
        password="your_password"
    )
    cursor = gymdb.cursor()
    get_members_in_age_range("25", "30")


except Error as e:
    print(f"Error: {e}")

finally:
    if gymdb and gymdb.is_connected():
        cursor.close()
        gymdb.close()
