#!/usr/bin/env python
# encoding: utf-8

from pyfiglet import Figlet
import PConstants
import sqlite3
import readline
import PDatabase

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
        elif command == PConstants.CMD_EXPORT:
            self.export_csv()
        elif command == PConstants.CMD_IMPORT:
            self.import_csv()    
        elif splt_command[0] == PConstants.CMD_HIDE:
            self.hide_entry()
        elif splt_command[0] == PConstants.CMD_DELETE:
            self.delete_entry(splt_command)
        elif splt_command[0] == PConstants.CMD_REVEAL:
            self.show(splt_command, 1)
        elif splt_command[0] == PConstants.CMD_SEARCH:
            self.search()
        elif splt_command[0] == PConstants.CMD_SHOW:
            self.show(splt_command, 0)
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
        self.print_help_command("count", "Count entries in database")
        self.print_help_command("delete", "Delete specific entry in database. Required argument: ID")
        self.print_help_command("exit", "Exits the password manager")
        self.print_help_command("export", "Export credentials as CSV-File in password secured zip file")
        self.print_help_command("help", "Prints this wonderful message")
        self.print_help_command("hide", "Hide entry in database. Required argument: ID")
        self.print_help_command("import", "Import CSV-File with credentials")
        self.print_help_command("reveal", "Reveal password of specific entry. Required argument: ID")
        self.print_help_command("login", "Authenticate with Email and Password")
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
            self.print_message("Error while trying to connect to database. \nError:\n" + str(e), 1)


    def add_entry(self):
        """
        Add new entry to db.
        :return:
        """
        title = input("Please enter title of new credential entry: ")
        username = input("username: ")
        password = input("password: ")
        url = input("url (optional): ")

        if title and username and password:
            PDatabase.insert(title, username, password, url)
            self.print_message("Successfully added credentials!", 0)
        else:
            self.print_message("Title, username and password cannot be empty!", 1)


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


    def delete_entry(self, cmd):
        """
        Delete entry in db.
        :return:
        """
        id = 0

        if len(cmd) > 1:
            id = cmd[1]
        else:
            id = input("Enter ID: ")
        
        if not PDatabase.check_if_id_exists(id):
            self.print_message("Record with ID " + id + " does not exist.", 1)
            return None

        self.show(["show", str(id)], 0)
        delete_bool = input("Are you sure you want to permanently delete this record?(y/n) ")

        if delete_bool == "y":
            try:
                connection = sqlite3.connect(PConstants.PASSPY_DATABASE_FILE)
                cursor = connection.cursor()
                cursor.execute('DELETE FROM credentials WHERE id = ' + str(id))
                connection.commit()
                self.print_message("Record #" + str(id) + " successfully deleted.", 0)
            except Exception as e:
                self.print_message("Record doesn't exist.", 1)
                return
        else:
            self.print_message("process aborted.", 0)


    def export_csv(self):
        """
        Export contents of SQLite DB as CSV-File
        """


    def import_csv(self):
        """
        Import credentials in CSV-file in PassPy-Format
        Title;Username;Password;URL (optional);
        """
        self.print_message("File must be in following format: title;username;password;url(optional, can be left blank)", 0)
        import_file_path = input("Please specify (absolute) path to csv-file: ")
        
        with open (str(import_file_path)) as import_file:
            line = import_file.readline()
            cnt = 1
            while line:
                splitted_line = line.split(";")
                self.insert_line(splitted_line, cnt)
                line = import_file.readline()
                cnt+=1


    def insert_line(self, splitted_line, cnt):
        """
        Check if line has right format and insert into db
        """
        if len(splitted_line) >= 3 and self.check_format(splitted_line):
            if len(splitted_line) == 4:
                PDatabase.insert(splitted_line[0].strip(), splitted_line[1], splitted_line[2], splitted_line[3])
            else:
                PDatabase.insert(splitted_line[0], splitted_line[1], splitted_line[2])
        else:
            self.print_message("There was error importing credentials at line #" + str(cnt), 1)                


    def check_format(self, splitted_line):
        """
        Check if first three elements are filled
        """
        for i in range(3):
            if str(splitted_line[i].strip()):
                pass
            else:
                return False

        return True


    def search(self):
        """
        Implements search function to db
        (returns more than one result, if found)
        :return:
        """


    def show(self, cmd, rev):
        """
        Implements search function to db
        (returns only data if search term is correct)
        :return:
        """
        id = 0

        if len(cmd) > 1:
            id = cmd[1]
        else:
            id = input("Enter ID: ")

        if not PDatabase.check_if_id_exists(id):
            self.print_message("Record with ID " + id + " does not exist.", 1)
            return None

        try:
            connection = sqlite3.connect(PConstants.PASSPY_DATABASE_FILE)
            cursor = connection.cursor()
            cursor.execute('SELECT * from credentials where id = ' + str(id))
            cur_result = cursor.fetchone()
            self.print_credentials(cur_result, rev)
        except Exception as e:
            self.print_message("Error while trying to connect to database. \nError:\n" + str(e), 1)
            return


    def print_credentials(self, cred, rev):
        """
        Print credentials formatted
        """
        print(PConstants.CLI_NEWLINE + "ID:\t\t" + str(cred[0]))
        print("Title:\t\t" + cred[1])
        print("Username:\t" + cred[2])
        if (rev == 0):
            print("Password:\t" + PConstants.CMD_ATT_SAMPLE_PW)
        else:
            print("Password:\t" + cred[3].strip())
        print("URL:\t\t" + cred[4].strip())
        print("Creation Date:\t" + cred[5])
        print("Hidden:\t\t" + cred[6] + PConstants.CLI_NEWLINE)        