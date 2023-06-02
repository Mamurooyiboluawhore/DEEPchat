#!/usr/bin/python3


import asyncio
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

# async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
#    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot command, type what I can respond to")

if __name__ == "__main__":
    from sys import argv

    application = ApplicationBuilder().token(argv[1]).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()