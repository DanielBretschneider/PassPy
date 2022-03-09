#!/usr/bin/env python
# encoding: utf-8

from pyfiglet import Figlet
import PConstants
import sqlite3
import readline

from PDatabase import print_message


class PConsole:
    """
    Console (CLI) Handler with following functionalities:
    * processes commands
    * shows help message
    """

    def __init__(self):
        """
        Constructors
        """
        pass

    def welcome_message(self):
        """
        Prints welcome message on program start
        """
        figlet = Figlet(font='slant')
        print(figlet.renderText("PassPy"), end='')
        print(PConstants.VERSION)
        print(PConstants.COPYRIGHT + PConstants.CLI_NEWLINE)

    def start(self):
        """
        Start console loop
        :return:
        """
        while True:
            command = self.read_command()
            self.process_command(command)

    def read_command(self):
        """
        Get command from user via input and return as string
        :return:
        """
        command = input(PConstants.CLI_PROMPT)
        return command

    def process_command(self, command):
        """
        Process given command
        :return:
        """
        command = command.lower().rstrip().lstrip()
        splt_command = command.split(" ")

        if command == "":
            pass
        elif command == PConstants.CMD_EXIT:
            exit()
        elif command == PConstants.CMD_HELP:
            self.print_help_message()
        elif command == PConstants.CMD_COUNT:
            self.print_db_count()
        elif command == PConstants.CMD_ADD:
            self.add_entry()
        elif command == PConstants.CMD_LOGIN:
            self.login()
        elif splt_command[0] == PConstants.CMD_HIDE:
            self.hide_entry()
        elif splt_command[0] == PConstants.CMD_DELETE:
            self.delete_entry()
        elif splt_command[0] == PConstants.CMD_SEARCH:
            self.search()
        elif splt_command[0] == PConstants.CMD_SHOW:
            self.show()
        else:
            self.print_message("Command '" + command + "' not found.", 1)

    def print_message(self, text, type):
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

    def print_help_message(self):
        """
        Print help message

        :return:
        """
        print("\nCommand | Description")
        print("-----------------------------------------")

        self.print_help_command("add", "Add new set of credentials")
        self.print_help_command("login", "Authenticate with Email and Password")
        self.print_help_command("count", "Count entries in database.")
        self.print_help_command("delete", "Delete specific entry in database. Required argument: ID")
        self.print_help_command("exit", "Exits the password manager")
        self.print_help_command("help", "Prints this wonderful message")
        self.print_help_command("hide", "Hide entry in database. Required argument: ID")
        self.print_help_command("reveal", "Reveal password of specific entry. Required argument: ID")
        self.print_help_command("search", "Searches for entries. Optional arguments: ID, Title, username, URL")
        self.print_help_command("show", "Shows specific entry. Required argument: ID")

        print(PConstants.CLI_NEWLINE)

    def print_help_command(self, command, description):
        """
        Line for command
        :param command: string
        :return:
        """
        print(PConstants.CLI_COL_BOLD + command + PConstants.CLI_COL_END +
              PConstants.CLI_TAB + description)

    def print_db_count(self):
        """
        Prints the number of entries in db
        :return:
        """ 
        try:
            connection = sqlite3.connect(PConstants.PASSPY_DATABASE_FILE)
            cursor = connection.cursor()
            cursor.execute('SELECT COUNT(*) from credentials')
            cur_result = cursor.fetchone()
            print("Total: " + str(cur_result[0]))
        except Exception as e:
            print_message("Error while trying to connect to database. \nError:\n" + str(e), 0)

    def add_entry(self):
        """
        Add new entry to db.
        :return:
        """

    def login(self):
        """
        Login / Authenticate
        :return:
        """

    def hide_entry(self):
        """
        Hide entry in db
        :return:
        """

    def add_entry(self):
        """
        Add entry!
        :return:
        """

    def delete_entry(self):
        """
        Delete entry in db.
        :return:
        """

    def search(self):
        """
        Implements search function to db
        (returns more than one result, if found)
        :return:
        """

    def show(self):
        """
        Implements search function to db
        (returns only data if search term is correct)
        :return:
        """