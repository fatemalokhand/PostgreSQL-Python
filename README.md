# COMP3005

# Assignment 3 - Question 1

# Name: Fatema Lokhandwala

# SN: 101259465

## Objective

This project implements CRUD (Create, Read, Update, Delete) operations on a PostgreSQL database using Python.

---

## Application Functions

- getAllStudents(): Retrieves and displays all records from the students table.
- addStudent(): Insert a new student record into the students table.
- updateStudentEmail(): Updates the email address for the student with the specified student_id.
- deleteStudent(): Deletes the record of the student with the specified student_id.

---

## Need to have

- Python v3.8 or higher must be installed
- PostgreSQL must be installed and running via pgAdmin
- psycopg2 library

---

## Instructions to setup and run the application

In your terminal, in the project's root directory, do this:

```bash
pip install psycopg2-binary
```

In order to connect to the database, do the following:

1. Open pgAdmin
2. Expand Servers from the left hand panel. Note: Connect to your PostgreSQL server if you haven't done so already
3. To create a new database, do the following:
   - Under your server, right click Databases
   - Click Create > Database...
   - Enter a name and hit Save
4. Expand the database you just created. Click on the database name to select it.
5. Select the Query Tool button.
6. Once in the Query Tool, select Open File
7. Select the file called students_table.sql. The SQL code should load into the editor.
8. Select the Execute/Refresh button to execute the script.
9. Expand the database, go to Schemas > public > Tables. The students table should appear there.
10. In the same Query Tool window, clear the content of the editor.
11. Select Open File.
12. Select the file called initial_data.sql. The SQL code should load into the editor.
13. Select Execute/Refresh to execute the script.

Open the file called main.py. In the file, update this line of code:

```bash
database_connection = psycopg2.connect(database="", user="", password="", host="localhost", port=5432)
```

and include your PostgreSQL credentials: database, user, password, host

To run the application, enter:

```bash
python main.py
```

---

## Video Link

Here's the link to my video:
