#Setting up and starting the bot
from bot.core import startBot
from ExpensesTrackerBot.util.settings import loadSettings

def main():
    startBot(loadSettings()["bot"])

if __name__ == "__main__":
    main()