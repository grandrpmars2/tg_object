import logging
from aiogram import Bot, Dispatcher
import config

logging.basicConfig(level=logging.INFO)

if not config.BOT_TOKEN:
	exit('Token is not provided')

bot = Bot(config.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)