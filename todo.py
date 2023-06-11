#!/usr/bin/env python3

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler, PicklePersistence
from settings import  TELEGRAM_BOT_TOKEN, CUSTOM_REPLIES

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Define the states of the conversation
TASK, DELETE = range(2)


# Define the start function
async def start_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """ start_bot: to start Bot """
    await context.bot.send_message(chat_id=update.effective_chat.id,
                     text='Hi! This is your todo list. You can add tasks by sending me messages.\n'
                                        'To see your tasks, use the /tasks command.\n'
                                        'To delete a task, use the /delete command.\n'
                                        'Send /cancel to stop the conversation.')

    return TASK

# A function to let users create todo
async def create_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """"
    Create_task: To create Todo
    """
    message_id = update.effective_message.message_id
    message_text = update.effective_message.text
    todo_title = message_text.replace("/new ", "")
    context.user_data[message_id] = {"title": todo_title, "completed": False}
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Todo successfully created")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
    Available commands:
    /start => start bot
    /create_task => creat todo
    /show_todo => show list of todos
    /new => Make a new Todo
    /list => To show list of Todos
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

# A function to view todo
async def show_todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text="Here are the list of todos:\n"
    for key, value in context.user_data.items():
        text += "- " + value
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

if __name__ == '__main__':
    my_persistence =PicklePersistence(filepath='todo')
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).persistence(my_persistence).build()

    create_handler = CommandHandler('new', create_task)
    application.add_handler(create_handler)

    start_handler = CommandHandler('start', start_bot)
    application.add_handler(start_handler)

    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)

    show_handler = CommandHandler('show', show_todo)
    application.add_handler(show_handler)

    application.run_polling()

