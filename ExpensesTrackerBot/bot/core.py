#Module that handles the backand business logic and connects to telegram
import logging
from telegram.ext import Updater, CommandHandler


def start(update, context):
    startMessage = "I'm the ExpensesTrackerBot. I will keep track of your and your friends expenses.\n\n"
    startMessage += "Following commands are currently avaiable:\n"
    startMessage += "/start: Replay this message\n"
    startMessage += "/addUser <username>: Add this person to the tracked list (name must be unique)\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=startMessage)

def addUser(update, context):
    pass

def startBot(botSettings, database):
    updater = Updater(token=botSettings["key"], use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
    startHandler = CommandHandler("start", start)
    newUserHandler = CommandHandler("newUser", addUser)
    dispatcher.add_handler(startHandler)
    dispatcher.add_handler(newUserHandler)
    updater.start_polling()