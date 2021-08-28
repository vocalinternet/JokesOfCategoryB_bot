import requests
import random
from bs4 import BeautifulSoup
import telebot
bot = telebot.TeleBot("ВСТАВЬТЕ ТОКЕН ВАШЕГО БОТА СЮДА")

def parse_joke(): # Парс анекдотов c указанного url
    num = random.randint(1, 1000)
    url = 'https://baneks.ru/' + str(num)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    joke = soup.find("p").text
    return joke

markup = telebot.types.InlineKeyboardMarkup()
markup1 = telebot.types.InlineKeyboardMarkup()

new_user = telebot.types.InlineKeyboardButton(text='Пришли анекдот',callback_data='new_user')
another_joke = telebot.types.InlineKeyboardButton(text='Ещё анекдот',callback_data='another_joke')

markup.add(new_user)
markup1.add(another_joke)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'Привет! Я бот, который присылает случайные анекдоты категории "Б"', reply_markup=markup)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, 'Разработчик: @calvision\nАнекдоты взяты с сайта: https://baneks.ru/')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'new_user':
        bot.send_message(call.message.chat.id, parse_joke(), reply_markup=markup1)
    elif call.data == 'another_joke':
        bot.send_message(call.message.chat.id, parse_joke(), reply_markup=markup1)


bot.polling()




