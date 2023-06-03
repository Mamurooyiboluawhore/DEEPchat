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

    ################################################################################# 
    ##                      Here comes DeepChat Power                              ##
    #################################################################################

async def todolist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
        This function gets/fetch info from google calender
    
    """

    await context.bot.send_message(chat_id=update.effective_chat.id, text=None)
    pass




if __name__ == "__main__":
    from sys import argv

    application = ApplicationBuilder().token(argv[1]).build()
    
    """
        Command Handlers to handle /start, /help, /todolist and (more to come) commands
    """

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    todolist_handler = CommandHandler('todolist', todolist)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(todolist)

    application.run_polling()