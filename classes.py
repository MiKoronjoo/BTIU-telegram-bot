import enum

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


class User:
    def __init__(self, user_id):
        self.id = user_id
        self.state = State.MAIN_MENU

    def back(self):
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

    def say(self, message):
        if message == bl_back:
            self.back()
            return

        elif message == bl_goto_main:
            self.state = State.MAIN_MENU
            return

        elif self.state == State.MAIN_MENU:
            if message == bl_taste_of_tea:
                self.state = State.TASTE_OF_TEA
                return
            elif message == bl_soalino:
                self.state = State.SOALINO
                return
            elif message == bl_contact_us:
                return ''

        elif self.state == State.TASTE_OF_TEA:
            if message == bl_fragrant_lines:
                self.state = State.FRAGRANT_LINES
                return
            elif message == bl_what_is_taste_of_tea:
                return ''
            elif message == bl_introduction:
                self.state = State.INTRODUCTION
                return

        elif self.state == State.SOALINO:
            if message == bl_soalino_98:
                self.state = State.SOALINO_98
                return
            elif message == bl_what_is_soalino:
                return ''

        elif self.state == State.SOALINO_98:
            if message == bl_soalino_question:
                return ''
            elif message == bl_soalino_send_answer:
                return ''

        elif self.state == State.INTRODUCTION:
            # TODO: send 'message' to admin
            return

        elif self.state == State.FRAGRANT_LINES:
            if message == bl_want_to_read:
                self.state = State.WANT_TO_READ
                return
            elif message == bl_want_to_send:
                self.state = State.WANT_TO_SEND
                return

        elif self.state == State.WANT_TO_READ:
            # TODO: send the book that related to 'message'
            return

        elif self.state == State.WANT_TO_SEND:
            # TODO: send 'message' to admin
            return

        raise InputError('"%s" is not a standard input' % message)
