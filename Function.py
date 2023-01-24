from Config import *
from Listas import *
from datetime import datetime
import telebot
import datetime as dt

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

meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

def monthtxt(month_number):
    if month_number == '01':
        return "enero"
    elif month_number == '02':
        return "febrero"
    elif month_number == '03':
        return "marzo"
    elif month_number == '04':
        return "abril"
    elif month_number == '05':
        return "mayo"
    elif month_number == '06':
        return "junio"
    elif month_number == '07':
        return "julio"
    elif month_number == '08':
        return "agosto"
    elif month_number == '09':
        return "septiembre"
    elif month_number == '10':
        return "octubre"
    elif month_number == '11':
        return "noviembre"
    elif month_number == '12':
        return "diciembre"
    else:
        return "Numero de mes invalido"    

@bot.message_handler(commands=["mundial"])
def cmd_start(message):
    bot.reply_to(message, "Faltan" + " " + str(diff.days) + " " + "días!")

@bot.message_handler(commands=["help"])
def cmd_help(message):
    bot.reply_to(message, "Si necesitas ayuda preguntale a google!")

@bot.message_handler(commands=['echo'])
def echo(message):
    chat_id = message.chat.id
    text = message.text[6:]  # Get the text of the message, excluding the '/echo' command
    bot.send_message(chat_id, text)

@bot.message_handler(commands=['info'])
def cmd_info(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Esta es la lista de comandos:\n"
                        "/mundial - días para el mundial 2026\n"
                        "/help - podes encontrar toda la info importante\n"
                        "/echo- repite el mensaje que mandes después de echo\n"
                        "/info - este comando bobo\n"
                        "/prox - próximos 3 cumpleaños\n"
                        "/cumple - cumple de putos de menor a mayor\n"
                        "/cumplemes - cumple de putos del mes")

@bot.message_handler(commands=["cumple"])
def cmd_cumple(message):
    cumple=[]
    date=[]
    month=[]
    chat_id = message.chat.id
    for nombre, fecha_cumple in cumples_nos.items():
            fecha_cumple=fecha_cumple.split('-')
            cumple.append(nombre)
            date.append(fecha_cumple[0])
            month.append(fecha_cumple[1])
    bot.send_message(chat_id, (cumple[0]+ ' cumple el '+ date[0] + ' de '+ monthtxt(month[0]) + '\n' 
                            + cumple[1]+ ' cumple el '+ date[1] + ' de '+ monthtxt(month[1]) + '\n' 
                            + cumple[2]+ ' cumple el '+ date[2] + ' de '+ monthtxt(month[2]) + '\n'
                            + cumple[3]+ ' cumple el '+ date[3] + ' de '+ monthtxt(month[3]) + '\n'
                            + cumple[4]+ ' cumple el '+ date[4] + ' de '+ monthtxt(month[4]) + '\n'))

@bot.message_handler(commands=["prox"])
def cmd_prox(message):
    chat_id = message.chat.id
    next_three = []
    next_three_str = []
    for nombre, fecha_cumple in cumple.items():
        fecha_cumple=fecha_cumple.split('-')
        if fecha_cumple[1] == today2[1]:
            if fecha_cumple[0] >= today2[0]:
                next_three.append(nombre+' cumple el '+ fecha_cumple[0] + ' de ' + meses[(int(fecha_cumple[1])) - 1])
        if len(next_three) == 3:
            break
    if len(next_three) < 3:
        for nombre, fecha_cumple in cumple.items():
            fecha_cumple=fecha_cumple.split('-')
            if len(next_three) < 3:
                if int(fecha_cumple[1]) == int(today2[1])+1:
                    next_three.append(nombre+' cumple el '+ fecha_cumple[0] + ' de ' + meses[(int(fecha_cumple[1])) - 1])
            if len(next_three) == 3:
                break
    next_three[2]=next_three[1]
    next_three[1]='Francia segundo'
    next_three_str = "\n".join(next_three)
    bot.send_message(chat_id, 'Los próximos 3 en cumplir años son:' + '\n' 
                                + next_three_str)

@bot.message_handler(commands=['cumplemes'])

def cmd_mes(message):
    cumplemes=[]
    chat_id = message.chat.id
    for nombre, fecha_cumple in cumple.items():
        fecha_cumple=fecha_cumple.split('-')
        if fecha_cumple[1] == today2[1]:
            cumplemes.append(nombre+' '+ fecha_cumple[0])
    cumplemes_string = "\n".join(cumplemes)
    bot.send_message(chat_id, 'Los que cumplen este mes:\n' + cumplemes_string)

def cmd_start_auto():
    bot.send_message(BOCA_CID, "Faltan" + " " + str(diff.days) + " " + "días!")

def cmd_mes_auto():
    cumplemes=[]
    for nombre, fecha_cumple in cumple.items():
        fecha_cumple=fecha_cumple.split('-')
        if fecha_cumple[1] == today2[1]:
            cumplemes.append(nombre + ' de ' + meses[(int(fecha_cumple[1])) - 1])
    cumplemes_string = "\n".join(cumplemes)
    bot.send_message(BOCA_CID, 'Los que cumplen este mes:\n' + cumplemes_string)

def recibir_mensajes():
    bot.infinity_polling()