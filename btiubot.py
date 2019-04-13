import time

import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

from config import *
from consts import *
from classes import *


def handle_chat(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if chat_type == u'private':
        if content_type == 'text':
            user = User(chat_id)
            try:
                user.say(msg['text'])
            except StateError:
                bot.sendMessage(chat_id, 'ERROR')
            except InputError:
                bot.sendMessage(chat_id, 'BAD INPUT')


bot = telepot.Bot(BOT_TOKEN)
MessageLoop(handle_chat, bot).run_as_thread()

while True:
    time.sleep(30)
