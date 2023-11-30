from aiogram import types
from data.config import ADMINS, CHANNEL
from loader import dp, bot


database_movies = "data/movies.txt"

@dp.message_handler(content_types=types.ContentTypes.VIDEO, user_id = ADMINS)
async def movie_register(msg: types.Message):
    result = await bot.copy_message(chat_id=CHANNEL, 
                           from_chat_id=msg.from_user.id, 
                           message_id=msg.message_id)
    if result:
        with open(database_movies, mode="a+") as f:
            f.write(f"{result.message_id}\n")
        await msg.answer(f"Kino kanalga 🆔 {result.message_id} bilan yuklandi.")
    else:
        await msg.answer("Kino kanalga yuklanmadi.")
