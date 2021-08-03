from aiogram import types
from dispatcher import dp, bot
import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputFile
import os
from handlers.recognize.obj import object_detection
import time
import math

@dp.message_handler(commands=['start'])
async def echo(message : types.Message):
	photo_button = InlineKeyboardButton('Распознать объект', callback_data='recognize object')
	inline_kb = InlineKeyboardMarkup().add(photo_button)
	await message.answer('Привет, я - умный бот Crowley. Могу распозновать и вырезать людей из фотографий.\nДля этого введи команду /photo', reply_markup=inline_kb)

@dp.message_handler(content_types=['photo'])
async def photo(message : types.Message):
	if config.recognize_process == True:
		config.recognize_process = False

		await message.answer('Идёт обработка фото. Обычно процесс длится до минуты.')
		try:
			cur_time = time.time()
			await message.photo[-1].download(f'handlers/recognize/{message.from_user.id}.jpg')
			persons = int(object_detection(f'handlers/recognize/{message.from_user.id}.jpg', f'handlers/recognize/{message.from_user.id}_output.jpg'))
			await bot.send_photo(message.from_user.id, InputFile(f'handlers/recognize/{message.from_user.id}_output.jpg'))
			for person in range(1, persons + 1):
				await bot.send_photo(message.from_user.id, InputFile(f'segmented_object_{person}.jpg'))
				os.remove(f'segmented_object_{person}.jpg')
			os.remove(f'handlers/recognize/{message.from_user.id}_output.jpg')
			os.remove(f'handlers/recognize/{message.from_user.id}.jpg')
			await message.answer(f'Вот твои фото. Процесс занял: {str(math.trunc(cur_time - time.time())).replace("-", "")} секунд.')
		except TypeError:
			await message.answer('На фото нет людей. Попробуйте снова или выберите другое фото.')
