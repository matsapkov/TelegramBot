import telebot
import random
from config import token
import time
import schedule
import datetime
from DB_class import DB
from schedule import every, repeat
import threading

db = DB()
bot = telebot.TeleBot(token)
hour, minute = 0, 0


@repeat(every(24).hours)
def get_random_time():
    global hour, minute, seconds
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    return hour, minute


def send_compliment(chat_id):
    compliment = db.get_random_compliment()
    print(compliment)
    if compliment:
        bot.send_message(chat_id, compliment)


def get_chat_id():
    chats_id = db.  get_chatID()
    return chats_id


@repeat(every(1).minute)
def schedule_daily_task():
    global hour, minute, seconds
    chats_id = get_chat_id()
    chats_id = set(map(lambda x: int(x[0]), chats_id))
    for chat_id in chats_id:
        print(f"Scheduled compliment at {hour}:{minute} for Chat: {chat_id}")
        print(datetime.datetime.now())
        if datetime.datetime.now().hour == hour and datetime.datetime.now().minute == minute:
            send_compliment(chat_id)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    nickname = str(message.from_user.first_name)
    name = str(message.from_user.last_name)
    db.put_user_in_db(chat_id, nickname, name)
    bot.send_message(chat_id, 'Вас приветствует самый любвеобильный бот в Телеграмме!')
    print(f'ChatID: {chat_id}')


if __name__ == '__main__':
    get_random_time()

    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)

    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()
    bot.polling(none_stop=True)
