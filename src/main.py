import telebot
from import_book import *
import os.path

TOKEN = "1138379542:AAHs7ZBVT1Q0o25iDgubW2q04dO2CZZfElc"
bot = telebot.TeleBot(TOKEN)
data_base = dict()

@bot.message_handler(commands=['help'])
def send_answer(message):
	reply = '''This application helps you to read books every day!
	Please, use command:
	/set_frequency [frequency]
	to set the frequency of sending chapters of the book'''
	#cur_book = book(os.path.dirname(__file__) + '/../witcher.html')
	#cur_book.open_html_book()
	#reply = cur_book.get_chapt(5)
	print(reply)
	bot.send_message(message.chat.id, reply)

@bot.message_handler(commands=['set_book'])
def set_book(message):
	bot.reply_to(message, 'Book has been set!')

@bot.message_handler(commands=['set_frequency'])
def set_frequency(message):
	bot.reply_to(message, 'Frequency has been set!')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()