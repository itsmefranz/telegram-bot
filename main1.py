import constants as keys
from telegram.ext import *
import responses as R

print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Type your message here to get started!')

def help_command(update, context):
    update.message.reply_text('If you need help.. you can consult Google for it!')

def handle_message(update, context):
    text = str(update.message.text).lower
    response = R.sample_responses(text)

    update.message.reply_text(response)

