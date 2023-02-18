import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = telegram.bot(token='TOKEN')
updater = Updater(token='TOKEN', use_context=True) #Replace TOKEN with your token string
dispatcher = updater.dispatcher