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
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This function initializes a conversation with the bot.... 
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
   """
    This function guides users on which commands to use....
   """
   text = """
/start    =>       Starts a Convesation with DeepChat
/todolist =>       Tells DeepChat to get ready for TodoList Creation
/help     =>       Guidains command 
"""
   await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    ################################################################################# 
    ##                      Here comes DeepChat's Power                              ##
    #################################################################################


async def todolist_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
        This function gets/fetch info from google calender
    
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, this is your to-do list")
    pass


if __name__ == "__main__":
    from sys import argv

    application = ApplicationBuilder().token(argv[1]).build()
    
    """
    Command Handlers to handle /start, /help, /todolist and (more to come) commands
    """
    start_handler = CommandHandler('start', start_command)
    help_handler = CommandHandler('help', help_command)
    todolist_handler = CommandHandler('todolist', todolist_command)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(todolist_handler)

    # Polling
    application.run_polling()