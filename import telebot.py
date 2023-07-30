import telebot

bot = telebot.TeleBot(6671810950:AAEguF8JfD-Fx404hXYsX020ZCZRQUGO1Sk)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Bienvenido a la votacion elige por quien deseas votar.")

@bot.message_handler(func=lambda message: message.text != "/start")
def vote(message):
    bot.send_message(message.chat.id, "Gracias por votar por {}!".format(message.text))

bot.polling()
