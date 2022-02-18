from telebot import *

import pytube


bot = TeleBot("5212513987:AAGdbwLwJFLZuL583AMnERhia7UYI1gXpMc")

def download(url):
    video = pytube.YouTube(url).streams.get_highest_resolution().download("./Video")
    return video

def videotitle(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    
    return video.title

@bot.message_handler(commands=['start'])
def main(message):
    bot.delete_message(message.chat.id,message.message_id)
    bot.send_photo(
        chat_id=message.chat.id,
        photo='https://vk.vkfaces.com/858224/v858224022/20475d/4mWIMR9MzNY.jpg',
        caption="<a href='https://github.com/000bakhtiyor'>Github</a>\n\n<b>Салом , Ботга хуш келибсиз ! Мен YouTubeдан видеоларни юклаб бераман. Бунинг учун сиз менга видео манзилини жўнатишингиз керак.\n\nНамуна : https://www.youtube.com/watch?v=7QJgJ5w9VI0</b>",
        parse_mode='html',
        )

@bot.message_handler(content_types=['text'])
def text(message):
    try:
        if "https://" in message.text:
            url = message.text
            bot.delete_message(message.chat.id,message.message_id)
        
            bot.send_message(
                chat_id=message.chat.id,
                text="<a>Видео : {0} \n</a><b>юклаб олинмоқда !</b>".format(url),
                parse_mode='html',
            )
            download(url)
            video = open('./Video/{0}.mp4'.format(videotitle(url)), 'rb')
            bot.send_message(
                chat_id=message.chat.id,
                text="<a>Видео : {0} \n</a><b>юклаб олинди !\n\nВидео телеграм чатга юкланмоқда.</b>".format(url),
                parse_mode='html',
            )
            bot.send_video(
                chat_id=message.chat.id,
                data = video,
                caption= "@YouTubeUzRobot",
            )
    except:
        bot.send_message(
            chat_id=message.chat.id,
            text="<b>Опсс! 😔 Видео юклаб олинмади ?!</b>",
            parse_mode='html',
        )
    


bot.polling(none_stop=True)