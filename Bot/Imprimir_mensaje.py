from Config import *
import telebot
import time
import sched
import datetime as dt

bot = telebot.TeleBot(TELEGRAM_TOKEN)

today = dt.date.today()
future = dt.date(2026,6,8)
diff = future - today
print(diff.days)

scheduler = sched.scheduler(time.time, time.sleep)

def imprimir_mensaje():
  bot.send_message(BOCA_CID, "Faltan" + " " + str(diff.days) + " " + "días!")