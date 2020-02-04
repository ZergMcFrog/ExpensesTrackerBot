#Module that handles the backand business logic and connects to telegram
from telegram.ext import Updater, CommandHandler
import logging

token = "TOKEN"
updater = Updater(token=token , use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)

def start(update, context):
    startMessage = "I'm the ExpensesTrackerBot. I will keep track of your and your friends expenses.\n\n"
    startMessage += "Following commands are currently avaiable:\n"
    startMessage += "/start: Replay this message\n"
    startMessage += "/addUser <username>: Add this person to the tracked List\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=startMessage)

def addUser(update, context):
    raise NotImplementedError

startHandler = CommandHandler("start", start)
dispatcher.add_handler(startHandler)
updater.start_polling()