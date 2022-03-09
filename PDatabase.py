#!/usr/bin/env python
# encoding: utf-8

import os
import sqlite3
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
        create_directory(PConstants.PASSPY_DATABASE_PATH)
        f = open(PConstants.PASSPY_DATABASE_FILE, "w")
        f.close()
    else:
        if not os.path.isfile(PConstants.PASSPY_DATABASE_FILE):
            print_message("PassPy database not found. Creating file '" + PConstants.PASSPY_DATABASE_FILE + "'", 1)
            f = open(PConstants.PASSPY_DATABASE_FILE, "w")
            f.close()
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
        print_message("PassPy directory already existed.", 1)    