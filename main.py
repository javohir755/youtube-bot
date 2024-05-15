TOKEN = '7186293978:AAFKLLH0mClneoVt7o4uWLMIKFat58m0VT4'






























# bot = telebot.TeleBot(TOKEN)
# @bot.message_handler(commands=['start'])
# def start_command(message):
#     bot.send_message(message.chat.id, "Assalomu alekum menga youtube link tashlang men sizga video formatda tashab beraman")
# @bot.message_handler(regexp=r'(https?://[^\s]+)')
# def handle_youtube_link(message):
#     youtube_url = message.text
#     try:
#         yt = YouTube(youtube_url)
#         video = yt.streams.filter(progressive=True, file_extension='mp4').first()
#         video_path = video.download()
#         bot.send_video(message.chat.id, open(video_path, 'rb'))
#     except Exception as e:
#         bot.send_message(message.chat.id, f"Error: {str(e)}")
# bot.polling()
