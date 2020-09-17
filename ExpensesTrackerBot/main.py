#Setting up and starting the bot
import json
from bot.core import startBot
from database.database import Database
from database.exceptions import InstanceAlreadyExistsException

def loadSettings():
    '''Loads the settings from given JSON formatted file'''
    with open("ExpensesTrackerBot/settings.json") as settingsFile:
        return json.load(settingsFile)

def main():
    settings = loadSettings()
    try:
        Database.setConfig(settings["bot"])
    except InstanceAlreadyExistsException:
        print("There is already an instance") #TODO replace with proper logging
    startBot(settings["bot"])

if __name__ == "__main__":
    main()