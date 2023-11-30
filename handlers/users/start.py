from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

database_users = "data/users.txt"



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    print(message)
    with open(database_users, mode="r+") as uf:
        users = uf.readlines()
    user_ids = set()
    for user in users:
        user_ids.add(int(user.strip()))

    if message.from_user.id in user_ids:
        await message.answer(f"Hush kelibsiz, {message.from_user.full_name}!")
    else:
        with open(database_users, mode="a+") as f:
            f.write(f"{message.from_user.id}\n")
        await message.answer(f"Siz muvafaqiyatli ro'yxatdan o'tdingiz, {message.from_user.full_name}!")
    

