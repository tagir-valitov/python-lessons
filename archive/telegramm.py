from telebot import types
import telebot
import webbrowser
import requests


bot = telebot.TeleBot('6993647708:AAEIVKce74tuU4Emz_kOHmovp_7VPEOTNvM')#
API ='baf810b8d72076e247aab1a890a25a3f'


@bot.message_handler(commands=['start', 'Hello!'])
def main(message):
    bot.send_message(message.chat.id,f'{message.from_user.first_name}, тебя приветствует семья <b>Валитовых</b>',parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://openweathermap.org/{city}&appid={API}&units=metric')
    bot.reply_to(message, f'Сейчас погода{res.json()}')


@bot.message_handler(commands=['Help'])
def main(message):
    bot.send_message(message.chat.id,message)


@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('http://hh.ru')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='http://yandex.com'))
    markup.add(types.InlineKeyboardButton('Удалить фото', callback_data='delete'))
    bot.reply_to(message,'Нашей семье нравится это фото!!', reply_markup=markup)


bot.infinity_polling()