# importing psycopg2 library for connecting to the PostgreSQL database
import psycopg2
from psycopg2 import sql

# creating and returning a PostgreSQL database connection
def db_connection():
    try:
        # the configuration for connecting to the database
        # Note: Replace these parameters (database, user, password, host) with your actual PostgreSQL credentials!!!!
        database_connection = psycopg2.connect(database="student_database", user="postgres", password="@DatabaseSystems1", host="localhost", port=5432)
        return database_connection
    # error handling
    except Exception as err:
        print(f"There was an error connecting to the database: {err}")
        return None

# getAllStudents function that retrieves and displays all students from the students table
def getAllStudents():
    database_connection = None
    cursor = None
    try:
        # establishing the database connection
        database_connection = db_connection()
        if database_connection is None:
            return
        cursor = database_connection.cursor()
        # executing the SQL query to select all the data from the students table
        cursor.execute("SELECT * FROM students ORDER BY student_id;")
        # getting all the data
        data = cursor.fetchall()
        print("\nHere are all the students:")
        for d in data:
            print(d)
    # error handling
    except Exception as err:
        print(f"There was an error in getting the students: {err}")
    finally:
        if cursor:
            # closing the cursor
            cursor.close()
        if database_connection:
            # closing the database connection
            database_connection.close()

# addStudent method that adds a new student into the students table
def addStudent(first_name, last_name, email, enrollment_date):
    database_connection = None
    cursor = None
    try:
        # establishing the database connection
        database_connection = db_connection()
        if database_connection is None:
            return
        cursor = database_connection.cursor()
        # SQL query to insert a new student into the students table
        insert_query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"
        data = (first_name, last_name, email, enrollment_date)
        # executing the query
        cursor.execute(insert_query, data)
        # committing the transaction
        database_connection.commit()
        print(f"Successfully added a new student, {first_name} {last_name}, into the students table.")
    # error handling
    except Exception as err:
        if database_connection:
            # if there's an error, performing a rollback
            database_connection.rollback()
        print(f"\nThere was an error in inserting the student: {err}")
    finally:
        if cursor:
            # closing the cursor
            cursor.close()
        if database_connection:
            # closing the database connection
            database_connection.close()

# updateStudentEmail method that updates the email address for a student with the specified student_id
def updateStudentEmail(student_id, new_email):
    database_connection = None
    cursor = None
    try:
        # establishing the database connection
        database_connection = db_connection()
        if database_connection is None:
            return
        cursor = database_connection.cursor()
        # SQL query to update the email address of the student with the given student_id
        update_query = "UPDATE students SET email = %s WHERE student_id = %s;"
        data = (new_email, student_id)
        # executing the query
        cursor.execute(update_query, data)
        # committing the transaction
        database_connection.commit()
        print(f"Successfully updated the email for student_id {student_id}.")
    # error handling
    except Exception as err:
        if database_connection:
            # if there's an error, performing a rollback
            database_connection.rollback()
        print(f"\nThere was an error in updating the email of the student: {err}")
    finally:
        if cursor:
            # closing the cursor
            cursor.close()
        if database_connection:
            # closing the database connection
            database_connection.close()

# deleteStudent method that deletes the student with the specified student_id
def deleteStudent(student_id):
    database_connection = None
    cursor = None
    try:
        # establishing the database connection
        database_connection = db_connection()
        if database_connection is None:
            return
        cursor = database_connection.cursor()
        # SQL query to delete the student from the students table
        delete_query = "DELETE FROM students WHERE student_id = %s;"
        data = (student_id,)
        # executing the query
        cursor.execute(delete_query, data)
        # committing the transaction
        database_connection.commit()
        print(f"Successfully deleted student with student_id {student_id}.")
    # error handling
    except Exception as err:
        if database_connection:
            # if there's an error, performing a rollback
            database_connection.rollback()
        print(f"\nThere was an error in deleting the student: {err}")
    finally:
        if cursor:
            # closing the cursor
            cursor.close()
        if database_connection:
            # closing the database connection
            database_connection.close()

# performing the CRUD operations
if __name__ == "__main__":
    print("Performing the CRUD operations...\n")

    # displaying all the students from the students table
    #getAllStudents()
    
    # adding a new student to the database
    #addStudent("Mark", "Tomtom", "Mark.Tomtom@example.com", "2023-09-02")
    # displaying all the students from the students table
    #getAllStudents()
    
    # updating the email address of the student
    #updateStudentEmail(1, "newemail@example.com")
    # displaying all the students from the students table
    #getAllStudents()

    # deleting the student from the database
    #deleteStudent(3)
    # displaying all the students from the students table
    #getAllStudents()

    # updating the email address of the student
    #updateStudentEmail(2, "blahblah@example.com")
    # displaying all the students from the students table
    #getAllStudents()

    # adding a new student to the database
    #addStudent("Nancy", "Gill", "Nancy.Gill@example.com", "2024-07-02")
    # displaying all the students from the students table
    #getAllStudents()

    # adding a new student to the database
    #addStudent("Duglas", "Yale", "Duglas.Yale@example.com", "2021-07-05")
    # displaying all the students from the students table
    #getAllStudents()

    # deleting the student from the database
    #deleteStudent(1)
    # displaying all the students from the students table
    #getAllStudents()

