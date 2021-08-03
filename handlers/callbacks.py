import config
from dispatcher import dp
from aiogram import types

@dp.callback_query_handler(text_contains='recognize object')
async def func_settings(call : types.CallbackQuery):
	await call.message.answer('Пришли мне фото с людьми.')
	config.recognize_process = True