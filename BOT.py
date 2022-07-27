import telebot
import datetime

bot = telebot.TeleBot(<TOKEN>)
        
msg_count = 0
@bot.message_handler(content_types=['text'])
def handle_command_adminwindow(message):
    global msg_count
    current_time = datetime.datetime.now().hour
    if (current_time < 6):
        msg_count = msg_count + 1
        if (msg_count == 10):
            msg_count = 0
            bot.send_message(chat_id=message.chat.id,
                            text="Reply service is unavailable during the midnight",
                            parse_mode='HTML')
    else:
        msg_count = 0


bot.infinity_polling()