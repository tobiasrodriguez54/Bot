from Imprimir_mensaje import *
from Config import *
from datetime import datetime
import telebot
import datetime as dt
import threading

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

date_time = dt.datetime.strptime(current_time, "%H:%M:%S")
a_timedelta = date_time - dt.datetime(1900, 1, 1)
seconds = a_timedelta.total_seconds()

today = dt.date.today()
future = dt.date(2026,6,8)
diff = future - today

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["mundial"])
def cmd_start(message):
    bot.reply_to(message, "Faltan" + " " + str(diff.days) + " " + "días!")

def recibir_mensajes():
    bot.infinity_polling()

if __name__ == "__main__":
    print('Iniciando el bot')
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
    print('Bot Iniciado')

while seconds != 86400:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    date_time = dt.datetime.strptime(current_time, "%H:%M:%S")
    a_timedelta = date_time - dt.datetime(1900, 1, 1)
    seconds = a_timedelta.total_seconds()
    if seconds == 86400:
        imprimir_mensaje()