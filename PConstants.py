#!/usr/bin/env python3
# encoding: utf-8

from pathlib import Path

#
# GENERAL
#
COPYRIGHT = "(C) 2022 Daniel Bretschneider"
VERSION = "v1.2.5"


#
# PATHS
#
USER_HOME = str(Path.home())
PASSPY_DATABASE_PATH = USER_HOME + "/.passpy/"
PASSPY_DATABASE_FILE = PASSPY_DATABASE_PATH + "passpy.db"
PASSPY_DATABASE_EXPORT_FILE = USER_HOME + "/Downloads/passpy_export.zip"
PASSPY_AUTH_FILE = PASSPY_DATABASE_PATH + "auth.txt"


#
# CLI
#
CLI_MSG_INFO = "[*] "
CLI_MSG_ERR = "[-] "
CLI_NEWLINE = "\n"
CLI_TAB = "\t"
CLI_COL_END = '\033[0m'
CLI_COL_BOLD = '\033[1m'
CLI_PROMPT = CLI_COL_BOLD + "[passpy] > " + CLI_COL_END

# commands
CMD_ADD = "add"
CMD_COUNT = "count"
CMD_DELETE = "delete"
CMD_EXIT = "exit"
CMD_EXPORT = "export"
CMD_HELP = "help"
CMD_HIDE = "hide"
CMD_IMPORT = "import"
CMD_REVEAL = "reveal"
CMD_SHOW = "show"
CMD_SEARCH = "search"
CMD_UNHIDE = "unhide"

#
CMD_ATT_ENTRIES = "entries"
CMD_ATT_ID = "id"
CMD_ATT_TITLE = "title"
CMD_ATT_USERNAME = "username"
CMD_ATT_URL = "url"
CMD_ATT_SAMPLE_PW = "**************"
MAX_SEARCH_TERM_LENGTH = 3
ZIP_COMPRESS_LEVEL = 5

#
# DATABASE
#
SQL_STATEMENT_INITIAL_CREDENTIAL_TABLE = """
                                CREATE TABLE IF NOT EXISTS credentials (
                                    ID INTEGER PRIMARY KEY,
                                    TITLE TEXT NOT NULL,
                                    USERNAME TEXT NOT NULL,
                                    PASSWORD TEXT NOT NULL,
                                    URL TEXT,
                                    CREATION_DATE TEXT NOT NULL,
                                    HIDDEN TEXT NOT NULL
                                )"""
