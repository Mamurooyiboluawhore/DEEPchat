#!/usr/bin/python3

import asyncio
from sys import argv
import telegram
import telegram.ext


async def main():
    bot = telegram.Bot(argv[1])
    async with bot:
        print(await bot.get_me())
    #    print((await bot.get_updates())[0])
        await bot.send_message(text='Hi Emy', chat_id=956127600)


async def start_callback(update, context):
    user_says = " ".join(context.args)
    await update.message.reply_text("You said: " + user_says)



if __name__ == '__main__':
    asyncio.run(main())