# -*- coding: utf-8 -*-
import telebot
from os.path import exists

wc_file_name = 'bienvenida.txt'
token = 'Your bot tokken'
admin = Your_ID

if exists(wc_file_name):
  with open(wc_file_name) as f:
    wc_txt = f.read()
  if not wc_txt:
    wc_txt = 'Custom welcome message.'
    with open(wc_file_name,'w') as f:
      f.write(wc_txt)
else:
  wc_txt = 'Custom welcome message.'
  with open(wc_file_name,'w') as f:
      f.write(wc_txt)

bot = telebot.TeleBot(token)

def listener(messages):
  for m in messages:
    if m.content_type == 'new_chat_participant':
      cid = m.chat.id
      bot.send_message(cid, wc_txt)

bot.set_update_listener(listener)

@bot.message_handler(commands=['wc'])
def wc(m):
  cid = m.chat.id
  uid = m.from_user.id
  if uid == admin:
    if len(m.text.split()) == 1:
      bot.send_message(cid, "Uso del comando:\n\n`/wc <nuevo mensaje de bienvenida>`", parse_mode="Markdown")
    else:
      wc_txt = ' '.join(m.text.split()[1:])
      with open(wc_file_name,'w') as f:
        f.write(wc_txt)
      bot.send_message(cid, "Mensaje de bienvenida actualizado")

bot.polling(True)
