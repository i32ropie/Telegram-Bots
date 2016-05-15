# -*- coding: utf-8 -*-

import telebot
from telebot import types
import time
import subprocess


TOKEN = "<Token>"
admin = <ID Admin>

bot = telebot.TeleBot(TOKEN)

def listener(messages):
    for m in messages:
        if m.from_user.id == admin:
            if m.content_type == 'text':
                if m.text.startswith('get'):
                    pwd = subprocess.Popen('pwd', shell=True, stdout=subprocess.PIPE).stdout.read()
                    pwd = pwd[0:len(pwd)-1]
                    try:
                        bot.send_document( admin, open( pwd + '/' + m.text.split(':')[1] ) )
                    except:
                        bot.send_message( admin, "Error enviando el documento")
                else:
                    execute_command(m)
                print str(m.from_user.first_name) + " [" + str(m.chat.id) + "]: " + m.text

bot.set_update_listener(listener)


def execute_command(message):
    cid = message.chat.id
    result_command = subprocess.Popen(message.text, shell=True, stdout=subprocess.PIPE).stdout.read()
    try:
        bot.send_message( cid, result_command)
    except:
        exception = True
    else:
        exception = False
    
    if exception:
        if result_command == "":
            bot.send_message( cid, "Empty output")
        else:
            with open( 'tmp.txt', 'w') as f:
                f.write( result_command)
            bot.send_document( cid, open( 'tmp.txt', 'rb'))


bot.polling(none_stop=True)
