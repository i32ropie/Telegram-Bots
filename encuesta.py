# -*- coding: utf-8 -*-
import telebot
from telebot import types
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

TOKEN = '<TOKEN>'
bot = telebot.TeleBot(TOKEN)
markup = types.ForceReply(selective=False)

encuesta = {
    'encuesta': '',
    'respuestas' : [],
    }

votaciones = {}

admin = <ID ADMIN>

def listener(messages):
    for m in messages:
        cid = m.chat.id
        if m.content_type == 'text':
            mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text
            print mensaje

bot.set_update_listener(listener)

@bot.message_handler(commands=['encuesta'])
def command_pregunta(m):
    cid = m.chat.id
    if cid == admin:
        msg = bot.send_message( cid, "Escribe la pregunta", reply_markup=markup)
        bot.register_next_step_handler( msg, guardaEncuesta)

def guardaEncuesta(m):
    cid = m.chat.id
    if cid == admin:
        encuesta['encuesta'] = m.text
        msg = bot.send_message( cid, "Respuesta 1: ", reply_markup=markup)
        bot.register_next_step_handler( msg, respuestas)

def respuestas(m):
    cid = m.chat.id
    if cid == admin:
        if not m.text.startswith('/fin'):
            nEle = len(encuesta['respuestas']) + 2
            encuesta['respuestas'].append(m.text)
            msg = bot.send_message( cid, "Respuesta " + str(nEle) + ": ", reply_markup=markup)
            bot.register_next_step_handler( msg, respuestas)
        else:
            hideBoard = types.ReplyKeyboardHide()
            bot.send_message( cid, "Encuesta terminada. Enlace para votar: http://telegram.me/RaspB_bot?start=votar", reply_markup=hideBoard)

@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid > 0 and m.text == '/start votar' and encuesta['respuestas']:
        markup = types.ReplyKeyboardMarkup()
        markup.resize_keyboard = True
        for respuesta in encuesta['respuestas']:
            markup.add(respuesta)
        msg = bot.send_message( cid, encuesta['encuesta'], reply_markup=markup)
        bot.register_next_step_handler( msg, votar)

def votar(m):
    cid = m.chat.id
    if m.text in encuesta['respuestas']:
        markup = types.ReplyKeyboardHide()
        mensaje = str(m.from_user.first_name) + " (@" + str(m.from_user.username) + ")"
        votaciones[mensaje] = m.text
        bot.send_message( cid, "Voto añadido/actualizado", reply_markup=markup)
        bot.send_message( admin, mensaje + " ha votado.")

@bot.message_handler(commands=['resultados'])
def command_resultados(m):
    cid = m.chat.id
    if cid == admin and votaciones:
        mensaje = ""
        for key in votaciones:
            mensaje += key + ": " + votaciones[key] + "\n"
        bot.send_message( cid, mensaje)
    elif cid == admin and not votaciones:
        bot.send_message( cid, "Aún no ha votado nadie.")

@bot.message_handler(commands=['reset'])
def command_reset(m):
    if m.chat.id == admin:
        encuesta['encuesta'] = ''
        encuesta['respuestas'] = []
        votaciones.clear()
        bot.send_message( admin, "Todo reseteado")

bot.polling( none_stop=True)
