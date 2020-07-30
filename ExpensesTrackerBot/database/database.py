#Wrapper for the database connection

class Database():
    def __init__(self, settings):
        self.settings = settings
        self.type = settings["type"]
        databaseInstance = getattr(__import__("ExpensesTrackerBot.database.instances", fromlist=[self.type]), self.type)