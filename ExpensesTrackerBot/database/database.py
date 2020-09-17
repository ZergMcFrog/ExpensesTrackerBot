#singleton which handles the connection to the database backend
import sqlite3 as sqlite

class Database():
    class __Database():
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
            self.commit()

        def deleteUser(self, name):
            pass

        def chageUser(self, name, admin=False):
            pass
    #End of inner class for singleton

    __instance = None
    __config = None

    def __init__(self, config):
        if not Database.instance:
            Database.instance = Database.__Database(config)

    def getInstance(self):
        if Database.instance is None:
            Database.instance = Database.__Database(Database.__config)
        return Database.instance

    def setConfig(self, config): #TODO add sytax check
        Database.__config = config

Database.setConfig = classmethod(Database.setConfig)
Database.getInstance = classmethod(Database.getInstance)