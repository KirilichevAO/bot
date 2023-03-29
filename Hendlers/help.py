from loader import dp
from aiogram.types import Message

@dp.message_handler(commands=['help'])
async def help_command(message: Message):
    await message.answer('Бог поможет!')