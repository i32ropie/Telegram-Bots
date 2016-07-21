# -*- coding: utf-8 -*-
from collections import OrderedDict
import telebot
from telebot import types
import time
import sys
 
############################################
#                 DATOS                    #
############################################
reload(sys)
sys.setdefaultencoding("utf-8")
 
TOKEN = '<TOKEN>'
botname = '<YOUR BOT USERNAME>'
 
grupo = <ID Grupo>
 
normas = OrderedDict([
    ('1', 'No hacer flood'),
    ('2', 'No hacer spam'),
    ('3', 'Solo puede invitar a nuevos usuarios @Edurolp (Para mantener el control del grupo)'),
    ('4', 'El off-topic está permitido, pero sin exceso'),
    ('5', 'Intentad no hacer preguntas estilo: ¿Hola cómo hago un bot?')
    ])
 
comandos = OrderedDict([
    ('normas', 'Normas del grupo'),
    ('info', 'Información del grupo'),
    ('bots', 'Bots creados por gente del grupo o simplemente interesantes/útiles'),
    ('enlaces', 'Enlaces de interés a la hora de desarrollar bots etc...')
    ])
 
bots = OrderedDict([
    ('League_of_Legends_bot', 'Bot con información acerca del League of Legends creado por @Edurolp'),
    ('chistes_bot', 'Bot de chistes graciosísimos creado por @pelijaro'),
    ('MarianoRajoy_BOT', 'Bot que recuerda los "mejores" momentos de Mariano Rajoy creado por @JoseAntonioMR'),
    ('GonchoBot', 'Bot con un montón de comandos útiles y entretenidos creado por @entangle'),
    ('noticiaslolbot', 'Bot con las últimas noticias del League of Legends creado por @Garfieldrockero'),
    ('galegobot', 'Bot que traduce tu Telegram al gallego creado por @Gerardo'),
    ('lolnewsbot', 'Bot creado por @rogama25 que envía automáticamente noticias del League of Legends'),
    ('Neverhope_bot', 'Envía roto2, miramachos, te busca imágenes y videos de youtube. Creado por @Neverhope'),
    ('storebot', 'Bot que almacena información de muchísimos bots. Puedes subir tu bot para hacerlo conocido'),
    ('todobbot', 'Bot que sirve para organizarte lista de cosas para hacer'),
    ('weatherbot', 'Bot que ofrece pronóstico del tiempo.'),
    ('getmusicbot', 'Bot con el que descargar de maner sencilla música a partir de youtube o soundcloud'),
    ('BlackJackBot', 'Bot para jugar al black jack'),
    ('GMTBot', 'Bot con el cuál tener el control de varias zonas horarias'),
    ('B4TBot', 'Bot parecido a @storebot'),
    ('YouTobeSearchBot', 'Bot para hacer búsquedas de vídeos'),
    ('RealHodorBot', 'Hodor Hodor Hodor'),
    ('StrangerBot', 'Bot para contactar con gente desconocida'),
    ('safe_bot', 'Bot para cifrar mensajes'),
    ('GypsyBot', 'Bot con bastantes funcionalidades'),
    ('Paquebot', 'Bot para administrar tus bots creados en http://paquebot.io'),
    ('LatexBot', 'Bot que convierte texto en LaTex a imagen'),
    ('ImageBot', 'Bot para obtener imágenes o gifs'),
    ('PollBot', 'Bot para crear encuestas')
    ])

enlaces = OrderedDict([
    ('1', 'http://www.forocoches.com/foro/showthread.php?t=4491359 \nTutorial básico para desarrollar bots'),
    ('2', 'https://c9.io/ \nPágina donde hostear tu bot gratuitamente'),
    ('3', 'https://github.com/eternnoir/pyTelegramBotAPI \nAPI en python para desarrollar bots'),
    ('4', 'https://core.telegram.org/bots/api \nAPI de Telegram para desarrollar bots'),
    ('5', 'https://github.com/ineedblood/telegram-bot \nMúltiples funciones para añadir a tu bot'),
    ('6', 'https://github.com/i32ropie/Telgram-Bots \nRepositorio con bots interesantes.'),
    ('7', 'https://github.com/yagop/node-telegram-bot-api \nAPI en node para desarrollar bots'),
    ('8', 'http://paquebot.io/ \nPágina para desarrollar bots de otra manera'),
    ('9', 'http://storebot.me/ \nPágina con gran cantidad de bots y la posibilidad de subir tus propias creaciones'),
    ('10', 'http://botsfortelegram.com/ \nPágina con gran cantidad de bots y la posibilidad de subir tus propias creaciones'),
    ('11', 'http://jsonviewer.stack.hu/ \nPágina para dar formato a cadenas de Json'),
    ('12', 'https://github.com/akalongman/php-telegram-bot/ \nAPI en PHP para desarrollar bots')
    ])
 
bot = telebot.TeleBot(TOKEN)
 
############################################
#                 FUNCIONES                #
############################################
 
def command_normas(m):
    cid = m.chat.id
    mensaje = 'Normas:\n'
    for a,b in normas.iteritems():
        mensaje += a + ') ' + b + '\n'
    bot.send_message( cid, mensaje)
    print "Enviando normas..."
 
def command_info(m):
    cid = m.chat.id
    mensaje = 'Grupo de Telegram para gente interesada en el desarrollo de Bots.\n\nComandos disponibles:\n'
    for a,b in comandos.iteritems():
        mensaje += '/' + a + ': ' + b + '\n'
    mensaje += '\n->Si quieres que tu bot sea añadido a la lista de bots o tienes agún enlace interesante de añadir, escríbeme a @Edurolp\n\n->Si quieres añadir a alguien al grupo, dile que me escriba a @Edurolp poniendo su alias.'
    bot.send_message( cid, mensaje)
 
def command_bots(m):
    cid = m.chat.id
    mensaje = 'Bots:\n'
    for a,b in bots.iteritems():
        mensaje += '@' + a + ': ' + b + '\n'
    bot.send_message( cid, mensaje, disable_web_page_preview=True)
 
def command_enlaces(m):
    cid = m.chat.id
    mensaje = 'Enlaces de interés:\n'
    for a,b in enlaces.iteritems():
        mensaje += a + ') ' + b + '\n'
    bot.send_message( cid, mensaje, disable_web_page_preview=True)
 
 
 
############################################
#                 LISTENER                 #
############################################
 
def listener(messages):
    for m in messages:
        cid = m.chat.id
        if m.content_type == 'text':
            if cid > 0:
                mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text
            else:
                mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text
            f = open('log.txt', 'a')
            f.write(mensaje + "\n")
            f.close()
            print mensaje
        elif m.content_type == 'new_chat_participant':
            if cid == grupo:
                bot.send_message( cid, 'Bienvenido, échale un vistazo a las normas :)')
                command_normas(m)
        elif m.content_type == 'left_chat_participant':
            if cid == grupo:
                bot.send_sticker( cid, open( 'adios.webp', 'rb'), reply_to_message_id=int(m.message_id))
 
bot.set_update_listener(listener)
 
 
############################################
#                 COMANDOS                 #
############################################
 
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    comando = m.text[7:]
    if comando == 'normas':
        command_normas(m)
    elif comando == 'info':
        command_info(m)
    elif comando == 'bots':
        command_bots(m)
    elif comando == 'enlaces':
        command_enlaces(m)
 
@bot.message_handler(commands=['normas'])
def command_z1(m):
    cid = m.chat.id
    if cid == grupo:
        bot.reply_to( m, 'https://telegram.me/{}?start=normas'.format(botname))
 
@bot.message_handler(commands=['info'])
def command_z2(m):
    cid = m.chat.id
    if cid == grupo:
        bot.reply_to( m, 'https://telegram.me/{}?start=info'.format(botname))
   
@bot.message_handler(commands=['bots'])
def command_z3(m):
    cid = m.chat.id
    if cid == grupo:
        bot.reply_to( m, 'https://telegram.me/{}?start=bots'.format(botname))
 
@bot.message_handler(commands=['enlaces'])
def command_z4(m):
    cid = m.chat.id
    if cid == grupo:
        bot.reply_to( m, 'https://telegram.me/{}?start=enlaces'.format(botname))
 
############################################
#                 POLLING                  #
############################################
 
bot.polling(none_stop=True)
