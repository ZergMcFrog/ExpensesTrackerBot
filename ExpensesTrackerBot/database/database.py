#singleton which handles the connection to the database backend
import sqlite3 as sqlite
from ExpensesTrackerBot.util.settings import loadSettings
from ExpensesTrackerBot.database.exceptions import InstanceAlreadyExistsException

class Database():
    class __Database():
        def __init__(self, config):
            self.config = config
            self.connection = sqlite.connect(self.config["target"])
            self.cursor = self.connection.cursor()

        def startTransaction(self):
            self.cursor.execute("BEGIN TRANSACTION;")

        def commit(self):
            self.cursor.execute("COMMIT;")

        def rollback(self):
            self.cursor.execute("ROLLBACK;")

        def addUser(self, name, admin):
            self.startTransaction()
            self.cursor.execute("INSERT INTO user (name, admin) VALUES('{0}', {1});".format(name, admin))
            self.commit()

        def deleteUser(self, name):
            pass

    #End of inner class for singleton

    __instance = None
    __config = loadSettings()["database"]

    def __init__(self, config):
        if Database.__instance is not None:
            raise InstanceAlreadyExistsException
        Database.__instance = self

    @classmethod
    def getInstance(cls):
        if Database.__instance is None:
            Database.__instance = Database.__Database(Database.__config)
        return Database.__instance

    @classmethod
    def setConfig(cls, config): #TODO add syntax check
        Database.__config = config
        Database.getInstance()

    @classmethod
    def getConfig(cls):
        return Database.__config