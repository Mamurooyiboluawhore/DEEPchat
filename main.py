#!/usr/bin/python3


import asyncio
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Defining Functions
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
        This function initializes a conversation with the bot    
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
   """
        This function guides users on which commands to use
   """
   text = """

/start    =>       Starts a Convesation with DeepChat
/todolist =>       Tells DeepChat to get ready for TodoList Creation
/help     =>       Guidains command 
   
   """
   await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

if __name__ == "__main__":
    from sys import argv

    application = ApplicationBuilder().token(argv[1]).build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    application.add_handler(start_handler)
    application.add_handler(help_handler)

    application.run_polling()