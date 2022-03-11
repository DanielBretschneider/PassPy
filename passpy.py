#!/usr/bin/env python
# encoding: utf-8
# -----------------------------------------------------------
# Simple password manager written in python
#
# (C) 2022 Daniel Bretschneider, Wien
# Using GNU General Public License v3.0
# email daniel@bretschneider.cc
# -----------------------------------------------------------

import PConsole
import PDatabase


def setup():
    """
    Setup program sequence
    
    :return: None
    """
    # start console
    console = PConsole()
    console.welcome_message()
    console.login()

    # create / check db files
    PDatabase.create_database_if_not_exists()

    # begin
    console.start()


if __name__ == '__main__':
    """
    Main method

    :return: None
    """
    setup()
