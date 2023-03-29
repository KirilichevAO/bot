from loader import dp
from aiogram.types import Message
from Keybords import kb_main

@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    await message.answer('Да, да, я готов работать!\n Сделай выбор!!!', reply_markup=kb_main)