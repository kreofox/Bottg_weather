import telebot
import requests
import json

bot = telebot.TeleBot("TOKEN_BOT")
API = "TOKEN"

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hi, Write the name of your city: ")

@bot.message_handler(content_types=["text"])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get('https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Now the weather: {temp}')

        image = "sunny.png" if temp > 5.0 else "sun.png"
        file = open("/img/" + image, "rb")
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message,"The city is wrong ")

bot.polling(none_stop=True)