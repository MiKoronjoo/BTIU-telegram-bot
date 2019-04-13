import enum

import telepot

from consts import *


class State(enum.Enum):
    #
    MAIN_MENU = 'MAIN_MENU'
    ##
    TASTE_OF_TEA = 'TASTE_OF_TEA'
    ###
    FRAGRANT_LINES = 'FRAGRANT_LINES'
    ####
    WANT_TO_READ = 'WANT_TO_READ'
    ####
    WANT_TO_SEND = 'WANT_TO_SEND'
    ###
    INTRODUCTION = 'INTRODUCTION'
    ##
    SOALINO = 'SOALINO'
    ###
    SOALINO_98 = 'SOALINO_98'


class StateError(Exception):
    pass


class InputError(Exception):
    pass


class CommandError(Exception):
    pass


class User:
    def __init__(self, user_id: int) -> None:
        self.id = user_id
        self.state = State.MAIN_MENU

    def __eq__(self, number: int) -> bool:
        return self.id == number

    def back(self) -> None:
        if self.state in (State.TASTE_OF_TEA, State.SOALINO):
            self.state = State.MAIN_MENU

        elif self.state in (State.FRAGRANT_LINES, State.INTRODUCTION):
            self.state = State.TASTE_OF_TEA

        elif self.state in (State.WANT_TO_READ, State.WANT_TO_SEND):
            self.state = State.FRAGRANT_LINES

        elif self.state == State.SOALINO_98:
            self.state = State.SOALINO

        else:
            raise StateError('User in state "%s" can\'t back' % self.state.value)

    def say(self, message: str, bot: telepot.Bot) -> bool:
        if message == bl_back:
            self.back()
            return True

        elif message == bl_goto_main:
            self.state = State.MAIN_MENU
            return True

        elif self.state == State.MAIN_MENU:
            if message == bl_taste_of_tea:
                self.state = State.TASTE_OF_TEA
                return True
            elif message == bl_soalino:
                self.state = State.SOALINO
                return True
            elif message == bl_contact_us:
                bot.sendMessage(self.id, msg_contact_us, reply_markup=ikb_contact_us)
                return False

        elif self.state == State.TASTE_OF_TEA:
            if message == bl_fragrant_lines:
                self.state = State.FRAGRANT_LINES
                return True
            elif message == bl_what_is_taste_of_tea:
                bot.sendMessage(self.id, msg_what_is_taste_of_tea)
                return False
            elif message == bl_introduction:
                self.state = State.INTRODUCTION
                return True

        elif self.state == State.SOALINO:
            if message == bl_soalino_98:
                self.state = State.SOALINO_98
                return True
            elif message == bl_what_is_soalino:
                bot.sendMessage(self.id, msg_what_is_soalino)
                return False

        elif self.state == State.SOALINO_98:
            if message == bl_soalino_question:
                bot.sendMessage(self.id, msg_soalino_question)
                return False
            elif message == bl_soalino_send_answer:
                bot.sendMessage(self.id, msg_soalino_send_answer)
                return False

        elif self.state == State.INTRODUCTION:
            # TODO: send 'message' to admin
            self.back()
            return True

        elif self.state == State.FRAGRANT_LINES:
            if message == bl_want_to_read:
                self.state = State.WANT_TO_READ
                return True
            elif message == bl_want_to_send:
                self.state = State.WANT_TO_SEND
                return True

        elif self.state == State.WANT_TO_READ:
            # TODO: send the book that related to 'message'
            return False

        elif self.state == State.WANT_TO_SEND:
            # TODO: send 'message' to admin
            self.back()
            return True

        raise InputError('"%s" is not a standard input' % message)

    def command(self, cmd: str, bot: telepot.Bot) -> None:
        if cmd == '/start':
            bot.sendMessage(self.id, msg_start)

        elif cmd == '/main_menu':
            self.state = State.MAIN_MENU

        elif cmd == '/help':
            bot.sendMessage(self.id, msg_help)

        else:
            raise CommandError('Command "%s" is not valid' % cmd)
