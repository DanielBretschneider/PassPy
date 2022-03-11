#!/usr/bin/env python
# encoding: utf-8


import os
import sqlite3
import PConstants
from pytz import NonExistentTimeError
from datetime import datetime


def print_message(text, type):
        """
        Prints a formatted message to terminal.

        :param text: Message Content
        :param type: (int) INFO (0), ERROR (1)
        :return: None
        """
        if type == 1:
            print(PConstants.CLI_MSG_ERR + text)
        else:
            print(PConstants.CLI_MSG_INFO + text)


def create_database_if_not_exists():
    """
    Sets up the PassPy directory and database file.
    Creates them, if they are not already there.

    :return: None
    """
    if not os.path.exists(PConstants.PASSPY_DATABASE_PATH):
        # create path
        create_directory(PConstants.PASSPY_DATABASE_PATH)
        
        # create db file
        create_db_file()
    else:
        if not os.path.exists(PConstants.PASSPY_DATABASE_FILE):
            print_message("PassPy database not found. Creating file '" + PConstants.PASSPY_DATABASE_FILE + "'", 1)
            create_db_file()
        else:
            print_message("Connection to database established." + PConstants.CLI_NEWLINE, 0)


def create_directory(path): 
    """
    Creates given directory.

    :return: None
    """
    try:
        print_message("PassPy database not found. Creating file '" + PConstants.PASSPY_DATABASE_FILE + "'", 1)
        os.mkdir(path)
    except FileExistsError:
        print_message("There was an error creating directory " + PConstants.PASSPY_DATABASE_PATH, 1)


def create_db_file():
    """
    Creates the .db file and sets up 'credentials' table inside.

    :return: None
    """
    # create db file
    f = open(PConstants.PASSPY_DATABASE_FILE, "w")
    f.close()

    # create credentials table
    con = database_connection()
    create_database_table(con, PConstants.SQL_STATEMENT_INITIAL_CREDENTIAL_TABLE)


def init_auth_file():
    """
    (re-)creates the authentification data file. This method is also responsible for the
    registration process!

    :return: None
    """
    if not os.path.exists(PConstants.PASSPY_AUTH_FILE) or os.path.getsize(PConstants.PASSPY_AUTH_FILE) == 0:
        auth_file = open(PConstants.PASSPY_AUTH_FILE, "x")
        print_message("Registering. Please remember your login credentials!", 0)
        uname = input("username: ")
        passwd = input("password: ")

        if not uname or not passwd:
            print_message("Username or Password cannot be empty!", 1)
            return None

        auth_file.write(uname + PConstants.CLI_NEWLINE)
        auth_file.write(passwd + PConstants.CLI_NEWLINE)
        print_message("Thank you! Have fun and log in to use passpy." + PConstants.CLI_NEWLINE, 0)
        auth_file.close()
    

def database_connection():
    """
    Connect to SQLite Database and return connection.

    :return: connection to PassPy database
    """
    connection = None

    # create connection
    try:
        # connect to db
        connection = sqlite3.connect(PConstants.PASSPY_DATABASE_FILE)
        return connection
    except Exception as e:
        print_message("There was a problem connecting to the database.", 1)
        print_message("Check if file '" + PConstants.PASSPY_DATABASE_FILE + "' exists and restart PassPy.", 1)
        exit()


def create_database_table(db_connection, create_table_sql_statement):
    """
    Create credentials table from the create_table_sql statement

    :param db_connection: Connection object
    :param create_table_sql_statement: a CREATE TABLE statement
    :return: None
    """
    try:
        # execute table creation statement
        cursor = db_connection.cursor()
        cursor.execute(create_table_sql_statement)
        db_connection.commit()
    except Exception as e:
        print_message("Error while executing sql-statement \n" + create_table_sql_statement + "\nError:\n" + str(e), 1)


def execute_query(query):
    """
    As the name above states. Is only used if no feedback
    or return value from database is needed.

    :return: None
    """
    try:
        # execute insert statement
        # connection to db
        db_connection = sqlite3.connect(PConstants.PASSPY_DATABASE_FILE)
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
    except Exception as e:
        print_message("Error while executing sql query. Error:\n" + str(e), 1)


def insert(title, username, password, url=""):
    """
    Builds an INSERT-Statement so new credentials can be easyly appended.

    :return: None
    """
    # create insert statement
    insert_statement = """INSERT INTO credentials (TITLE, USERNAME, PASSWORD, URL, CREATION_DATE, HIDDEN) VALUES ('""" + title + "', '" + username + "', '" + password + "', '" + url +\
                            "', '" + get_datetime_string() + "', '" + str(0) + "')"

    execute_query(insert_statement)
    

def get_datetime_string():
    """
    Get datetime.

    :return: Time and Date, please.
    """
    return str(datetime.now())


def check_if_id_exists(id):
    """
    Check if record with given id exists.
    If there is a record with a higher id, then it must have been deleted. 

    :return: None
    """
    try:
        connection = sqlite3.connect(PConstants.PASSPY_DATABASE_FILE)
        cursor = connection.cursor()
        cursor.execute('SELECT EXISTS(SELECT 1 FROM credentials WHERE id = ' + str(id) + ')')
        cur_result = cursor.fetchone()
        
        if cur_result[0] == 1:
            return True
        else:
            return False
    except Exception as e:
        print_message("Error while trying to connect to database. \nError:\n" + str(e), 1)


def check_if_record_hidden(id):
    """
    Check if specific record is hidden.

    :return: True, if record is hidden (1)
    """
    try:
        connection = sqlite3.connect(PConstants.PASSPY_DATABASE_FILE)
        cursor = connection.cursor()
        cursor.execute('SELECT HIDDEN FROM credentials WHERE id = ' + str(id))
        cur_result = cursor.fetchone()
        
        if cur_result[0] == "1":
            return True
        else:
            return False
    except Exception as e:
        print_message("Error while trying to connect to database. \nError:\n" + str(e), 1)


def get_count():
    """
    Get the total number of records stored in database.

    :return: Number of records in database as numeric string
    """
    try:
        connection = sqlite3.connect(PConstants.PASSPY_DATABASE_FILE)
        cursor = connection.cursor()
        cursor.execute('SELECT MAX(id) FROM credentials')
        cur_result = cursor.fetchone()
        return str(cur_result[0])
    except Exception as e:
        print_message("Error while trying to connect to database. \nError:\n" + str(e), 1)
