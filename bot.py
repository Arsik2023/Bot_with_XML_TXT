import telebot 

token = '6554668745:AAEpQzSIf3y7yfUSiALsBfm1782G_B0532c'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
@bot.message_handler(content_types=['text'])

def start_message(message):
    bot.send_message(message.chat.id,"Приветствую, мне нужен XML файл")
    bot.register_next_step_handler(message, func_work_xml)

def func_work_xml(message):
    bot.send_message(message.chat.id,"Это функция для XML")

    bot.register_next_step_handler(message, func_work_txt)

def func_work_txt(message):
    bot.send_message(message.chat.id,"Это функция для TXT")
    
bot.infinity_polling()