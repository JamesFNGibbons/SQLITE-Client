"""
    This class is used to manage the connection to the
    SQLite file. It will return an open piped connection
    to the file, for use in the command files.

    James Gibbons N0803836
    Nottingham Trent University
"""

import sqlite3

class Db:

    def __init__(self):
        self.con = sqlite3.connect('./db/database.db')

    def close(self):
        self.con.close()
