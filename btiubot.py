import pprint
import time

import telepot
from telepot.loop import MessageLoop

from config import BOT_TOKEN, hidden_code
from classes import *

users = []


def handle_chat(msg: dict) -> None:
    # pprint.pprint(msg)
    # return
    global users
    # users: list
    content_type, chat_type, chat_id = telepot.glance(msg)
    if chat_type == u'private':
        if chat_id not in users:
            if content_type == 'text' and msg['text'] == '/start ' + hidden_code:
                this_user = BtiuUser(chat_id)
            else:
                this_user = User(chat_id)
            users.append(this_user)
        else:
            this_user = users[users.index(chat_id)]
            if content_type == 'text' and msg['text'] == '/start ' + hidden_code:
                if type(this_user) != BtiuUser:
                    users.remove(this_user)
                    this_user = BtiuUser(chat_id)
                    users.append(this_user)

        if content_type == 'text':
            try:
                if msg['text'][0] == '/':
                    send_message = this_user.command(msg['text'], bot)

                else:
                    if this_user.state in BtiuUser.INFO_STATES:
                        send_message = this_user.say_info(msg['text'], bot)
                    else:
                        send_message = this_user.say(msg['text'], bot)

                if send_message:
                    bot.sendMessage(chat_id, msg_state[this_user.state.value],
                                    reply_markup=rkb_state[this_user.state.value])
            except StateError:
                bot.sendMessage(chat_id, err_bad_input)
            except InputError:
                bot.sendMessage(chat_id, err_bad_input, reply_markup=rkb_state[this_user.state.value])
            except CommandError:
                bot.sendMessage(chat_id, err_bad_cmd, reply_markup=rkb_state[this_user.state.value])
            except AssertionError:
                bot.sendMessage(chat_id, err_free_time)

        elif this_user.state == State.PICTURE:
            if content_type == 'photo':
                bot.sendMessage(chat_id, err_photo)
            elif content_type == 'document':
                if msg['document']['file_size'] > 10 * 1024 * 1024:
                    bot.sendMessage(chat_id, err_size)
                else:
                    this_user.file_id = msg['document']['file_id']
                    this_user.state = State.UNIVERSITY
                    bot.sendMessage(chat_id, msg_state[this_user.state.value],
                                    reply_markup=rkb_state[this_user.state.value])


bot = telepot.Bot(BOT_TOKEN)
MessageLoop(bot, handle_chat).run_as_thread()

while True:
    time.sleep(30)
