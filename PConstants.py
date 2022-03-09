#!/usr/bin/env python3
# encoding: utf-8

from pathlib import Path

#
# GENERAL
#
COPYRIGHT = "(C) 2022 Daniel Bretschneider"
VERSION = "v1.1.3"


#
# PATHS
#
USER_HOME = str(Path.home())
PASSPY_DATABASE_PATH = USER_HOME + "/.passpy/"
PASSPY_DATABASE_FILE = PASSPY_DATABASE_PATH + "passpy.db"

#
# CLI
#
CLI_PROMPT = "[passpy] > "
CLI_MSG_INFO = "[*] "
CLI_MSG_ERR = "[-] "
CLI_NEWLINE = "\n"
CLI_TAB = "\t"
CLI_COL_END = '\033[0m'
CLI_COL_BOLD = '\033[1m'

# commands
CMD_ADD = "add"
CMD_LOGIN = "login"
CMD_COUNT = "count"
CMD_DELETE = "delete"
CMD_EXIT = "exit"
CMD_HELP = "help"
CMD_HIDE = "hide"
CMD_REVEAL = "reveal"
CMD_SHOW = "show"
CMD_SEARCH = "search"

#
CMD_ATT_ENTRIES = "entries"
CMD_ATT_ID = "id"
CMD_ATT_TITLE = "title"
CMD_ATT_USERNAME = "username"
CMD_ATT_URL = "url"