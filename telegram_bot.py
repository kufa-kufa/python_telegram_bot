import telebot
import pyowm

owm = pyowm.OWM('1a14b2b38cf250d1ff5a0365c1e4c0a3',language='ru')
bot = telebot.TeleBot("835629663:AAGW5rnCSv3yYQIJXUbWIixWqxsdTkJeVZQ")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    #bot.reply_to(message, message.text)
    #answer = 'Простите мы не смогли найти ваш город'
    try:
        observation = owm.weather_at_place(message.text)
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]    
        answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
        answer += "Температура сейчас " + str(temp) + "\n" 
        if temp < 12:
            answer += "Пожалуйста одевайтесь по теплее, на улице холодно!"+"\n"
    except:
        answer = 'Неверная информация, попробуйте еще раз и выясните ошибки пожалуйста'
    bot.send_message(message.chat.id, answer)
bot.polling(none_stop= True)    
