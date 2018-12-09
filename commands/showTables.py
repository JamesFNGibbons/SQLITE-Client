from db_manager import Db

class showTables:

    def __init__(self):
        self.description = 'List all the tables in the database.'

    def on_run(self, params):
        db = Db()
        cursor = db.con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

        if(len(cursor.fetchall()) > 0):
            print(cursor.fetchall())
        else:
            print('There are no tables in the database.')
