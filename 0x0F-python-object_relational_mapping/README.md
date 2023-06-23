# Before you start...
Please make sure your MySQL server is in version 8.0. If you haven't installed MySQL 8.0 in Ubuntu 20.04 yet, here are the instructions:

## How to install MySQL 8.0 in Ubuntu 20.04

1. Open a terminal.

2. Install the `python3-dev` package by running the following command:
   ```
   sudo apt-get install python3-dev
   ```

3. Install the `libmysqlclient-dev` package:
   ```
   sudo apt-get install libmysqlclient-dev
   ```

4. Install the `zlib1g-dev` package:
   ```
   sudo apt-get install zlib1g-dev
   ```

5. Install the `mysqlclient` package using pip3:
   ```
   sudo pip3 install mysqlclient
   ```

   This will install the MySQLdb module version 2.0.x.

6. Verify the installation by opening the Python interpreter:
   ```
   python3
   ```

7. Import the MySQLdb module and check the version:
   ```python
   import MySQLdb
   print(MySQLdb.version_info)
   ```

   The output should be something like `(2, 0, 3, 'final', 0)`, indicating a successful installation.

8. Install the `SQLAlchemy` module using pip3:
   ```
   sudo pip3 install SQLAlchemy
   ```

   This will install SQLAlchemy version 1.4.x.

9. Verify the installation by opening the Python interpreter:
   ```
   python3
   ```

10. Import the SQLAlchemy module and check the version:
    ```python
    import sqlalchemy
    print(sqlalchemy.__version__)
    ```

    The output should be something like `'1.4.22'`, indicating a successful installation.

11. You may see a warning message related to `'@@SESSION.GTID_EXECUTED'`. You can ignore this warning for now.

That's it! You have now installed MySQL 8.0 and the required Python modules for this project.

## Background Context

In this project, you will explore the combination of two amazing worlds: Databases and Python!

The project consists of two parts:

**Part 1: Using MySQLdb**

In this part, you will utilize the `MySQLdb` module to connect to a MySQL database and execute SQL queries. The `MySQLdb` module provides a straightforward way to interact with MySQL databases using Python.

Here's an example of how you would use `MySQLdb` without an Object Relational Mapper (ORM):

```python
import MySQLdb

# Connect to the MySQL database
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()

# Execute an SQL query
cur.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all rows from the result
query_rows = cur.fetchall()

# Process the query result
for row in query_rows:
    print(row)

# Close the cursor and the database connection
cur.close()
conn.close()
```

**Part 2: Using SQLAlchemy**

In the second part, you will utilize the `SQLAlchemy` module, which is an Object Relational Mapper (ORM). The purpose of an ORM is to abstract the storage details and allow you to work with Python objects instead of writing SQL queries directly. This provides flexibility and makes it easier to switch between different storage systems without rewriting your entire codebase.

Here's an example of how you would use `SQLAlchemy` with an ORM:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from my_model import Base, State

# Create

 the database engine
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)

# Create the database tables (if they don't exist)
Base.metadata.create_all(engine)

# Create a session to interact with the database
session = Session(engine)

# Perform a query using the ORM
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))

# Close the session
session.close()
```

As you can see, with an ORM like `SQLAlchemy`, you no longer need to write explicit SQL queries. Instead, you can work with Python objects that map to database tables, making your code more intuitive and easier to maintain.

It's important to note that different ORM libraries may have slightly different syntax and features, so it's recommended to read tutorials and refer to the official documentation when using a specific ORM.

## Resources

To further explore the topics covered in this project, here are some recommended resources:

- [Object-relational mappers](https://en.wikipedia.org/wiki/Object-relational_mapping)
- [MySQLdb documentation](https://mysqlclient.readthedocs.io/)
- [MySQLdb tutorial](https://mysqlclient.readthedocs.io/user_guide.html)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Introduction to SQLAlchemy](https://www.datacamp.com/community/tutorials/introduction-to-sqlalchemy-in-python)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [10 common stumbling blocks for SQLAlchemy newbies](https://alextechrants.blogspot.com/2013/03/10-common-stumbling-blocks-for.html)
- [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
- [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
- [SQLAlchemy Tutorial](https://leportella.com/sqlalchemy-tutorial.html)

## Learning Objectives

By the end of this project, you are expected to be able to explain the following topics without the help of Google:

1. Why Python programming is awesome
2. How to connect to a MySQL database from a Python script
3. How to select rows in a MySQL table from a Python script
4. How to insert rows in a MySQL table from a Python script
5. What ORM means
6. How to map a Python Class to a MySQL table

## Copyright - Plagiarism

It is essential to approach the tasks in this project independently to meet the learning objectives mentioned above.

Copying and pasting someone else's work, in part or in whole, is strictly forbidden and will result in removal from the program.

You are not allowed to publish any content of this project.

Make sure to comply with the requirements listed below.

## Requirements

- General:
  - Allowed editors: vi, vim, emacs
  - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
  - Your files will be executed with MySQLdb version 2.0.x
  - Your files will be executed with SQLAlchemy version 1.4.x
  - All your files should end with a new line
  - The first line of all your files should be exactly `#!/usr/bin/python3`
  - A `README.md` file, at the root of the project folder, is mandatory
  - Your code should adhere to the pycodestyle (version 2

.8.\*) style guide
  - All your files must be executable
  - The length of your files will be tested using the `wc` command
  - All your modules should have a documentation (you can use the `python3 -c 'print(__import__("my_module").__doc__)'` command to verify)
  - All your classes should have a documentation (you can use the `python3 -c 'print(__import__("my_module").MyClass.__doc__)'` command to verify)
  - All your functions (inside and outside a class) should have a documentation (you can use the `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'` commands to verify)
  - A documentation is not a simple word; it is a sentence explaining the purpose of the module, class, or method. The length of the documentation will be verified.
  - You are not allowed to use `execute` with SQLAlchemy.

Make sure to install the required versions of MySQLdb and SQLAlchemy as specified in the instructions above.