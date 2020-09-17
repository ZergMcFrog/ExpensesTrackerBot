#Module that handles the backend business logic and connects to telegram
from sqlite3 import IntegrityError
from telegram.ext import Updater, CommandHandler
from ExpensesTrackerBot.database.database import Database as db

def start(update, context):
    startMessage = "I'm the ExpensesTrackerBot. I will keep track of your expenses.\n\n"
    startMessage += "Following commands are currently avaiable:\n"
    startMessage += "/start: Replay this message\n"
    startMessage += "/addUser <username>: Add this person to the tracked list (name must be unique and whitespaces are not allowed)\n"
    startMessage += "/addItem <itemname> <price/amount>: Add this item to the tracked list. Choose if the total price or amount should be tracked\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=startMessage)

def addUser(update, context):
    userInput = " ".join(context.args)
    userName = userInput.split(" ")[0]
    try:
        db.getInstance().addUser(userName, False)
    except IntegrityError:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Could not add user. Username {} has already been given".format(userName))
    context.bot.send_message(chat_id=update.effective_chat.id, text="User {} succesfully added!".format(userName))

def addItem(update, context):
    userInput = " ".join(context.args)
    item, price = userInput.split(" ")
    db.getInstance().addItem(item, price)


def startBot(botSettings):
    updater = Updater(token=botSettings["key"], use_context=True)
    dispatcher = updater.dispatcher
    startHandler = CommandHandler("start", start)
    newUserHandler = CommandHandler("addUser", addUser)
    newItemHandler = CommandHandler("addItem", addItem)
    dispatcher.add_handler(startHandler)
    dispatcher.add_handler(newUserHandler)
    dispatcher.add_handler(newItemHandler)
    updater.start_polling()