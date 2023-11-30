import asyncio
from aiogram import types
from data.config import ADMINS
from loader import dp, bot

database_users = "data/users.txt"

@dp.message_handler(commands="ads", user_id = ADMINS)
async def ads_sender_handler(msg: types.Message):
    reklama = msg.get_args()
    sender = await msg.answer("Yuborilmoqda.")
    with open(database_users, mode="r+") as uf:
        users = uf.readlines()

    for user in users:
        try:
            await bot.send_message(chat_id=int(user.strip()),
                               text=reklama)
            await asyncio.sleep(0.1)
        except Exception as e:
            print(e)
            continue
    await sender.edit_text("Yuborib bo'ldim.")