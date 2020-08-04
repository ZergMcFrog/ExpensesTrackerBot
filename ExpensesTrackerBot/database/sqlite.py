#Concrete implementation for connecting to sqlite databases
import sqlite3 as sqlite

class Database():

    def __init__(self, config):
        self.config = config
        self.connection = sqlite.connect(self.config["target"])
        self.cursor = self.connection.cursor()

    def startTransaction(self):
        self.cursor.execute("START TRANSACTION;")

    def commit(self):
        self.cursor.execute("COMMIT;")

    def rollback(self):
        self.cursor.execute("ROLLBACK;")

    def addUser(self, name, admin=False):
        self.startTransaction()
        self.cursor.execute("INSERT INTO user (name, admin) VALUES('{0}', {1});".format(name, admin))

    def deleteUser(self, name):
        pass

    def chageUser(self, name, admin=False):
        pass