# -*- coding: utf-8 -*-

import telebot
import time

bot = telebot.TeleBot('token')

def loading(to_sleep, sleeped):
    loaded_count = (sleeped/to_sleep)*100
    loaded_bar = "#"*int(loaded_count/10)+" "*(10-int(loaded_count/10))
    return loaded_bar, loaded_count

@bot.message_handler(commands=['load'])
def cmd(m):
    cid = m.chat.id
    splited = m.text.split()
    msg = bot.send_message(cid, "Loading\n\n`[          ] 0%`", parse_mode="Markdown")
    if len(splited) > 1:
        to_sleep = int(splited[1])
        sleeped = 0
        for x in range(to_sleep):
            for y in range(4):
                time.sleep(0.05)
                sleeped += 0.25
                loaded_bar, loaded_count = loading(to_sleep, sleeped)
                bot.edit_message_text("Loading\n\n`[" + loaded_bar + "] %2f%%`"%(loaded_count), cid, msg.message_id, parse_mode="Markdown")

bot.polling(True)
