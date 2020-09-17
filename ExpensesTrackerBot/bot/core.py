#Module that handles the backend business logic and connects to telegram
from telegram.ext import Updater, CommandHandler
from ExpensesTrackerBot.database.database import Database as db

def start(update, context):
    startMessage = "I'm the ExpensesTrackerBot. I will keep track of your expenses.\n\n"
    startMessage += "Following commands are currently avaiable:\n"
    startMessage += "/start: Replay this message\n"
    startMessage += "/addUser <username>: Add this person to the tracked list (name must be unique and whitespaces are not allowed)\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=startMessage)

def addUser(update, context):
    userInput = " ".join(context.args)
    userName = userInput.split(" ")[0]
    database = db.getInstance()
    database.addUser(userName, False)

def startBot(botSettings):
    updater = Updater(token=botSettings["key"], use_context=True)
    dispatcher = updater.dispatcher
    startHandler = CommandHandler("start", start)
    newUserHandler = CommandHandler("addUser", addUser)
    dispatcher.add_handler(startHandler)
    dispatcher.add_handler(newUserHandler)
    updater.start_polling()