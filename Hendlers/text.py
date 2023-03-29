from loader import dp
from aiogram.types import Message

@dp.message_handler(commands=['мама'])
async def help_command(message: Message):
    await message.answer('Ты смотри, маму он вспомнил!')
