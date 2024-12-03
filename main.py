import logging
from yandex_music import Client, track
from ya_music import ya_music
from aiogram import Dispatcher, Bot, types, executor
import requests
from config import YANDEX_USER_TOKEN, BOT_TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

client = Client(YANDEX_USER_TOKEN).init() # Токен пользователя Яндекс.Музыка (полное получение прописано в официальной документации)

@dp.message_handler(content_types=['text'])
async def send_welcome(msg: types.Message):
    
    async def download_send_music(music_id, music_name, music_artists): # Функция по отправке трека
        link = client.tracks_download_info(music_id, get_direct_links=True) # Получаем информацию о треке от API
        audios = requests.get(link[0].direct_link).content # Запрос на файл трека из API
        await bot.send_audio(msg.chat.id, audio=audios, title=music_name, performer=music_artists) # Отправляем аудио с исполнителем и названием 

    
    if msg.text == "/start":
        await msg.answer("Привет!\n\nЯ — бот для скачивания музыки из сервиса Яндекс Музыка. С моей помощью ты сможешь бесплатно скачивать любимые треки прямо к себе в Telegram.\n\nДля того, чтобы скачать трек, просто отправь мне его название. Если выдаст другой трек, пожалуйста, укажи дополнительно автора после названия трека.")
    else:
        search_result = ya_music.get_music_by_name(query=msg.text) # Обращаемся к классу из ya_music.py, получаем return ввиде массива из данных трека, либо просто False при ошибке
        if(not search_result):
            await msg.reply("Ошибка.\nЭто точно название трека?") # Поиск проходит по названию трека. Дальше выбирается самый популярный и отправляется юзеру
        else:
            await msg.answer(f'{search_result[0]}\nОтправляю...')
            await download_send_music(search_result[1], search_result[3], search_result[4])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)