#Setting up and starting the bot
import json
from bot.core import startBot
from database.database import Database

def loadSettings():
    '''Loads the settings from given JSON formatted file'''
    with open("ExpensesTrackerBot/settings.json") as settingsFile:
        return json.load(settingsFile)

def main():
    settings = loadSettings()
    database = Database(settings["database"])
    startBot(settings["bot"], database)

if __name__ == "__main__":
    main()