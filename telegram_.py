#!/usr/bin/python3

"""main file and it is subject to correction and modification"""


from sys import argv
import telegram
from telegram.ext import Updater

Token = argv[1]
updater = telegram.ext.Updater(Token, use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    update.message.reply_text("Hello. Welcome to DeepChat")


def emycodes(update, context):
    update.message.reply_text("Click here to learn more about emycodes: https://www.emycodes.tech")


def mamuro(update, context):
    update.message.reply_text("Click here to learn more about emycodes: https://www.mamuro.tech")


def niyero(update, context):
    update.message.reply_text("Click here to learn more about emycodes: https://www.niyero.tech")


def contact(update, context):
    update.message.reply_text("You may contact us on this website: https://www.deepchat.org/")


dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('emycodes', emycodes))
dispatcher.add_handler(telegram.ext.CommandHandler('mamuro', mamuro))
dispatcher.add_handler(telegram.ext.CommandHandler('niyero', niyero))
dispatcher.add_handler(telegram.ext.CommandHandler('contact', contact))

updater.start_polling()
updater.idle()