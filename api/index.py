from flask import Flask
from flask_telebot import TeleBot

app = Flask(__name__)
app.config['TELEBOT_TOKEN'] = '6294585980:AAH8WFD-CbbMfV6ZEtYV36m58qPGHvQTxjY'
bot = TeleBot(app)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Olá! Bem-vindo ao meu bot do Telegram.')

if __name__ == '__main__':
    bot.polling()
    app.run()
