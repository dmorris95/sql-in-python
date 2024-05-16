import mysql.connector
from mysql.connector import Error

#Task 1: Add new member
def add_member(id, name, age, trainer_id):
    try:
        exist_id = []
        id_select = "SELECT id From Members"
        cursor = gymdb.cursor()
        cursor.execute(id_select)
        id_check = cursor.fetchall()
        for x in id_check:
            x = str(x)
            for bad_char in '(,)':
                x = x.replace(bad_char, '')
            exist_id.append(x)
        #First attempt at finding exist ids, the code in Task 3 is much more efficient
        if id in exist_id:
            print("That id already exists, please enter a different ID")
        else:
            new_member = id, name, age, trainer_id
            insert_member = "INSERT INTO Members (id, name, age, trainer_id) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_member, new_member)
            gymdb.commit()
            print("New member has been successfully added.")
    except Error as e:
        print(f"Error: {e}")

#Task 2: Add workout session
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        new_workout = member_id, date, duration_minutes, calories_burned
        add_workout = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
        cursor.execute(add_workout, new_workout)
        gymdb.commit()
        print("Workout successfully added.")
    except Error as e:
        print(f"Error: {e}")


#Task 3: Update Member
def update_member(member_id, new_age):
    try:
        
        update_sql = "UPDATE Members SET age = %s WHERE id = %s"
        update_age = new_age, member_id
        #see if id exists
        check_sql = "SELECT * FROM Members WHERE id = %s"
        cursor.execute(check_sql, tuple(member_id))
        found = cursor.fetchall()
        if found == []:
            print("That user does not exist, please try again.")
        else:
            cursor.execute(update_sql, update_age)
            gymdb.commit()
            print("Member updated!")

    except Error as e:
        print(f"Error: {e}")


#Task 4: Delete a workout session
def delete_workout_session(session_id):
    try:
        delete_sql = "DELETE FROM WorkoutSessions WHERE session_id = %s"
        #check if session exist
        check_sql = "SELECT * FROM WorkoutSessions WHERE session_id = %s"
        cursor.execute(check_sql, tuple(session_id))
        found = cursor.fetchall()
        if found == []:
            print("Sorry, this session ID does not exist, please try a different session ID")
        else:
            cursor.execute(delete_sql, tuple(session_id))
            gymdb.commit()
            print("Session successfully deleted.")
    except Error as e:
        print(f"Error: {e}")

try: 
    gymdb = mysql.connector.connect(
        database = "gym_db",
        host="host_name",
        user="root",
        password="your_password"
    )
    cursor = gymdb.cursor()
    
    add_member("5", "Luke Butler", "43", "1")
    add_workout_session("4", "2024-06-05", "45", "124")
    update_member("4", "23")
    delete_workout_session("1")

except mysql.connector.Error as db_error:
    print("Database error: {db_error}")

except Error as e:
    print(f"Error: {e}")

finally:
    if gymdb and gymdb.is_connected():
        cursor.close()
        gymdb.close()
