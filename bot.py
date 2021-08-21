import telebot

bot = telebot.TeleBot("YOUR_BOT_ID")

@bot.message_handler(content_types = ['text'])
def send_echo(message):
    bot.reply_to(message, message.text)

bot.polling( none_stop = True )