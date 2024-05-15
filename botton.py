
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

menyu_buttonn = InlineKeyboardMarkup(row_width=2)
video_button = InlineKeyboardButton("Video 🎞", callback_data='video')
audio_button = InlineKeyboardButton("Audio 🔊", callback_data='audio')
menyu_buttonn.add(video_button, audio_button)
