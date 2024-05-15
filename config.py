# import asyncio
# import logging
# import sys
# import telebot
# from os import getenv
# from pytube import YouTube
# from aiogram import Bot, Dispatcher
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
# from aiogram.types import Message
# from main import TOKEN
# from pytube import YouTube
# from pytube.exceptions import RegexMatchError




















import asyncio
import logging
import sys
import telebot
from os import getenv
from pytube import YouTube
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
from main import TOKEN
from botton import menyu_buttonn

dp = Dispatcher()
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Assalomu alekum! YouTube linkini yuboring, undan keyin sizga video yoki audio formatda faylni yuboraman.Bot sizga javob yozishi uchun bir nima yozib yuboring:")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, "Video (🎞) yoki Audio (🔊)?", reply_markup=menyu_buttonn)

@bot.callback_query_handler(lambda call: call.data in ['video', 'audio'])
def handle_format_selection(call):
    if call.data == 'video':
        bot.send_message(call.message.chat.id, "YouTube linkini yuboring:")
        bot.register_next_step_handler(call.message, handle_video_link)
    elif call.data == 'audio':
        bot.send_message(call.message.chat.id, "YouTube linkini yuboring:")
        bot.register_next_step_handler(call.message, handle_audio_link)

def handle_video_link(message):
    youtube_url = message.text
    try:
        yt = YouTube(youtube_url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video_path = video.download()
        
        title = yt.title
        print(title)
        author = yt.author
        duration = yt.length
        a = int(duration) / 60
        b = int(duration) % 60
        bot.send_video(message.chat.id, open(video_path, 'rb'), caption=f"Video Nomi:\n{title},\nVideo Avtori:\n{author},\nSoati:\n{int(a)}:{b}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {str(e)}")

def handle_audio_link(message):
    youtube_url = message.text
    try:
        yt = YouTube(youtube_url)
        audio = yt.streams.filter(only_audio=True).first()
        audio_path = audio.download()
        title = yt.title
        author = yt.author
        duration = yt.length
        bot.send_audio(message.chat.id, open(audio_path, 'rb'), caption=f"{title},{author},")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {str(e)}")

bot.polling()






