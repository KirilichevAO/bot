from loader import dp
from DataBase import add_new_user, find_user, change_user, delete_user
from aiogram.types import Message
from Keybords import kb_main

@dp.message_handler(commands=['new'])
async def add_user(message: Message):
    name, phone, comment = message.text.split()[1:]
    tg_id = int(message.from_user.id)
    print(name, phone, comment)
    user = (name, tg_id, phone, comment)
    add_new_user(user)

@dp.message_handler(commands=['find'])
async def find_user_command(massage: Message):
    name = (massage.text.split()[1],)
    result = find_user(name)
    if not result:
        result = 'Такого пользователя нет!'
    await massage.answer(text=result)

@dp.message_handler(commands=['change'])
async def change_user_command(massage: Message):
    name = massage.text.split()[1]
    if not name.isdigit():
        await massage.answer(text=find_user((name,)))
    else:
        user_id, name, phone, comment = massage.text.split()[1:]
        new_user = (name, phone, comment, user_id)
        change_user(new_user)

@dp.message_handler(commands=['del'])
async def delete_user_command(massage: Message):
    user_id = massage.text.split()[1]
    if user_id.isdigit():
        delete_user((int(user_id),))
    else:
        await massage.answer('Надо прислать id юзера!')
