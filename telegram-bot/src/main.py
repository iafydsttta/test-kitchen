# Code takes inspiration from tutorial here:
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot

import asyncio
import logging
import os

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    ExtBot,
)
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['TELEGRAMTOKEN']

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Reduce relatively spammy httpx logging
logging.getLogger('httpx').setLevel(logging.WARNING)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
        text="This command does not do anything really. I'm a bot, please talk to me!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # all lines after first will be indented
    text =  \
        """
            Commands

            /start      :: Initialize chat with this bot
            /help       :: Show this help message
            /track      :: Track a ticker
        """

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

async def track(update: Update, context: ContextTypes.DEFAULT_TYPE):
    raise NotImplementedError

async def regular_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.debug(f"{update.effective_chat.id=}")
    await context.bot.send_message(chat_id=update.effective_chat.id,
        text="No smart LLM responses here. All hardcoded goodness.")

    # just echo:
    # await context.bot.send_message(chat_id=update.effective_chat.id,
    #                                text=update.message.text)

async def send_message_to_myself():
    app = ApplicationBuilder().token(TOKEN).build()
    bot: ExtBot = app.bot
    await bot.send_message(chat_id=os.environ['TELEGRAMCHATID'], text="Lorem Ipsum")

if __name__ == '__main__':
    RESPONSIVE = True
    # --------------------------------
    # How to run a responsive chat bot:

    if RESPONSIVE:
        app = ApplicationBuilder().token(TOKEN).build()
        start_handler = CommandHandler('start', start)
        help_handler = CommandHandler('help', help)
        track_handler = CommandHandler('track', track)
        text_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), regular_text)
        app.add_handler(start_handler)
        app.add_handler(help_handler)
        app.add_handler(track_handler)
        app.add_handler(text_handler)
        app.run_polling()
    # --------------------------------

    #  How to send a message without polling:
    if not RESPONSIVE:
        asyncio.run(send_message_to_myself())
    # --------------------------------
