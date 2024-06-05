import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    cht = message.chat.id

    bot.send_message(cht, f'Ватсап нігер!\nЮзай фрази з обережністю, бо я твою маму їбав :)')

@bot.message_handler(commands=['phrases'])
def phrases(message):
    cht = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    hello = types.KeyboardButton('hello')
    markup.add(hello)
    bot.send_message(cht, 'Обери потрібну фразу, відповідно до ситуації', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text(message):
    cht = message.chat.id
    text = message.text

    if text == 'hello':
        bot.send_voice(cht, open('voice/hello.wav', 'rb'))

bot.polling()