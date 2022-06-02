import settings
import calc
import telebot

bot = telebot.TeleBot(settings.BOT_TOKEN)


@bot.message_handler(commands=['calc'])
def calc(message):
    bot.send_message(message.chat.id, calc.calc(message), parse_mode='html')


bot.polling(none_stop=True)