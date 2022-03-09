#!/usr/bin/env python
# encoding: utf-8
# -----------------------------------------------------------
# Simple password manager written in python
#
# (C) 2022 Daniel Bretschneider, Wien
# email daniel@bretschneider.cc
# -----------------------------------------------------------

from PConsole import PConsole
import PConstants


def setup():
    """
    Setup program sequence

    :param self:
    :return:
    """
    console = PConsole()
    console.welcome_message()
    console.start()




if __name__ == '__main__':
    """
    Main method
    """
    setup()
