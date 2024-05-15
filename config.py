import asyncio
import logging
import sys
from os import getenv
import telebot
from pytube import YouTube
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from main import TOKEN
from botton import menyu_buttonn




dp = Dispatcher()
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Assalomu alekum menga youtube link tashlang men sizga video formatda tashab beraman🎞")
    
    
@bot.message_handler(regexp=r'(https?://[^\s]+)')
def handle_youtube_link(message):
    bot.send_message(message.chat.id,"Iltimos Kutib turing bot malumot toplayapdi🔧")
    youtube_url = message.text
    try:
        yt = YouTube(youtube_url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video_path = video.download()
        title = yt.title
        author = yt.author
        duration = yt.length
        description = yt.description
        bot.send_video(message.chat.id, open(video_path, 'rb'), caption=f"{title}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {str(e)}")
bot.polling()

async def main() -> None:
   
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())





