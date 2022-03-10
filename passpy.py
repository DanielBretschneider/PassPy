#!/usr/bin/env python
# encoding: utf-8
# -----------------------------------------------------------
# Simple password manager written in python
#
# (C) 2022 Daniel Bretschneider, Wien
# Using 
# email daniel@bretschneider.cc
# -----------------------------------------------------------

from PConsole import PConsole
import PConstants
import PDatabase


def setup():
    """
    Setup program sequence

    :param self:
    :return:
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
    """
    setup()
