from Config import *
from datetime import datetime
import telebot
import datetime as dt
import threading
from Function import *
import time

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

date_time = dt.datetime.strptime(current_time, "%H:%M:%S")
a_timedelta = date_time - dt.datetime(1900, 1, 1)
seconds = a_timedelta.total_seconds()

today = dt.date.today()
today2 = today.strftime("%d-%m-%Y")
today2=today2.split('-')

future = dt.date(2026,6,8)
diff = future - today

bot = telebot.TeleBot(TELEGRAM_TOKEN)

if __name__ == "__main__":
    print('Iniciando el bot')
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
    print('Bot Iniciado')

while seconds != 0:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    date_time = dt.datetime.strptime(current_time, "%H:%M:%S")
    a_timedelta = date_time - dt.datetime(1900, 1, 1)
    seconds = a_timedelta.total_seconds()
    today = dt.date.today()
    future = dt.date(2026,6,8)
    diff = future - today
    if seconds == 0:
        cmd_start_auto()
        cmd_mes_auto()
        time.sleep(86200)
    seconds=1