# Code takes inspiration from tutorial here:
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot

import logging

from telegram import Update
from telegram.ext import ContextTypes

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
            /track      :: Track a ticker, like "VWCE.DE"
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
