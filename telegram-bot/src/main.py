# Code takes inspiration from tutorial here: 
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

import os

TOKEN = os.environ['TELEGRAMTOKEN']

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
        text="This command does not do anything really. I'm a bot, please talk to me!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # all lines after first will be indented
    text =  \
        """
            Commands

            /start :: Initialize chat with this bot
            /help  :: Show this help message
        """

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

async def regular_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
        text="No smart LLM responses here. All hardcoded goodness.")
    
    # just echo:
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    app.add_handler(start_handler)
    app.add_handler(help_handler)

    text_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), regular_text)    
    app.add_handler(text_handler)
    
    app.run_polling() 
