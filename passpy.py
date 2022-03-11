#!/usr/bin/env python
# encoding: utf-8
# -----------------------------------------------------------
# Simple password manager written in python
#
# (C) 2022 Daniel Bretschneider, Wien
# Using GNU General Public License v3.0
# email daniel@bretschneider.cc
# -----------------------------------------------------------


import PDatabase
from PConsole import PConsole


def setup():
    """
    Setup program sequence
    
    :return: None
    """
    # create / check db files
    PDatabase.create_database_if_not_exists()
    
    # start console
    console = PConsole()
    console.welcome_message()
    console.login()

    # begin
    console.start()


if __name__ == '__main__':
    """
    Main method

    :return: None
    """
    setup()
