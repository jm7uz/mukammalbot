from aiogram import types
from data.config import CHANNEL

from loader import dp, bot

database_movies = "data/movies.txt"

# Echo bot
@dp.message_handler()
async def bot_echo(msg: types.Message):
    with open(database_movies, mode="r+") as uf:
        movies = uf.readlines()
    movie_ids = set()
    for user in movies:
        movie_ids.add(int(user.strip()))
    
    try:
        if int(msg.text) in movie_ids:
            await bot.copy_message(chat_id=msg.from_user.id, from_chat_id=CHANNEL, message_id=int(msg.text))
        else:
            await msg.answer("Bunday kino mavjud emas.")
    except:
        await msg.answer("Bunday kino mavjud emas.")