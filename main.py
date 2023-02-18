import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = telegram.bot(token='TOKEN')
updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')

hello()