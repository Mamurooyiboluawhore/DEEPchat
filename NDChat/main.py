import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
      #update.message.reply_text(
      #      'Hello {}'.format(update.message.from_user.first_name)
     # )
      first_name = update.message.from_user.first_name
      await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello {first_name}")

if __name__ == '__main__':
    application = ApplicationBuilder().token('6238081820:AAHPbErkU-33_oWkWasfUF4OfamSlxQpxts').build()
                
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    hello_handler = CommandHandler('hello', hello)
    application.add_handler(hello_handler)
                                
    application.run_polling()
