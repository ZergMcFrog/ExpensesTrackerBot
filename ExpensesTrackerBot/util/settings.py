import json

def loadSettings():
    '''Loads the settings from given JSON formatted file'''
    with open("ExpensesTrackerBot/settings.json") as settingsFile:
        return json.load(settingsFile)