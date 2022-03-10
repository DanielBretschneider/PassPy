#!/usr/bin/env python
# encoding: utf-8

import os
import sqlite3
from pytz import NonExistentTimeError
from datetime import datetime
import PConstants

def print_message(text, type):
        """
        Print message to terminal
        :param text: Message Content
        :param type: (int) INFO (0), ERROR (1)
        :return:
        """
        if type == 1:
            print(PConstants.CLI_MSG_ERR + text)
        else:
            print(PConstants.CLI_MSG_INFO + text)


def create_database_if_not_exists():
    """
    Creates the db file and directory, if not existing
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
            print_message("Connection to database established.", 0)


def create_directory(path): 
    """
    Create folder at <path>
    """
    try:
        print_message("PassPy database not found. Creating file '" + PConstants.PASSPY_DATABASE_FILE + "'", 1)
        os.mkdir(path)
    except FileExistsError:
        print_message("There was an error creating directory " + PConstants.PASSPY_DATABASE_PATH, 1)


def create_db_file():
    """
    Create and initalize db file
    """
    # create db file
    f = open(PConstants.PASSPY_DATABASE_FILE, "w")
    f.close()

    # create credentials table
    con = database_connection()
    create_database_table(con, PConstants.SQL_STATEMENT_INITIAL_CREDENTIAL_TABLE)


def database_connection():
    """
    Connect to SQLite Database
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
    create a table from the create_table_sql statement
    :param db_connection: Connection object
    :param create_table_sql_statement: a CREATE TABLE statement
    :return:
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
    As the name above states
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
    INSERT into 'credentials' table in database
    """
    # create insert statement
    insert_statement = """INSERT INTO credentials (TITLE, USERNAME, PASSWORD, URL, CREATION_DATE, HIDDEN) VALUES ('""" + title + "', '" + username + "', '" + password + "', '" + url +\
                            "', '" + get_datetime_string() + "', '" + str(0) + "')"

    execute_query(insert_statement)
    

def get_datetime_string():
    """
    Get datetime as string.
    """
    return str(datetime.now())


