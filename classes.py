import enum

import telepot


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
    # -------------------------#
    FULL_NAME = 'FULL_NAME'
    PICTURE = 'PICTURE'
    UNIVERSITY = 'UNIVERSITY'
    COMMITTEE = 'COMMITTEE'
    AGE = 'AGE'
    PHONE_NUMBER = 'PHONE_NUMBER'
    SHIRAZI = 'SHIRAZI'
    SCHOOL_INFO = 'SCHOOL_INFO'
    SCHOOL_TYPE = 'SCHOOL_TYPE'
    HOME_ADDR = 'HOME_ADDR'
    HAVE_CAR = 'HAVE_CAR'
    KNOWN_SCHOOLS = 'KNOWN_SCHOOLS'
    FREE_TIMES = 'FREE_TIMES'
    IDEA_AT_ALL = 'IDEA_AT_ALL'


from consts import *


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

    def command(self, cmd: str, bot: telepot.Bot) -> bool:
        if cmd == '/start':
            bot.sendMessage(self.id, msg_start)
            return True

        elif cmd == '/main_menu':
            self.state = State.MAIN_MENU
            return True

        elif cmd == '/help':
            bot.sendMessage(self.id, msg_help, reply_markup=rkb_state[self.state.value])
            return False

        elif cmd.startswith('/start '):
            bot.sendMessage(self.id, msg_info)
            self.state = State.FULL_NAME
            return True

        else:
            raise CommandError('Command "%s" is not valid' % cmd)


class BtiuUser(User):
    INFO_STATES = [State.FULL_NAME, State.PICTURE, State.UNIVERSITY, State.COMMITTEE, State.AGE, State.PHONE_NUMBER,
                   State.SHIRAZI, State.SCHOOL_INFO, State.SCHOOL_TYPE, State.HOME_ADDR, State.HAVE_CAR,
                   State.KNOWN_SCHOOLS, State.FREE_TIMES, State.IDEA_AT_ALL]

    def __init__(self, user_id: int) -> None:
        super().__init__(user_id)
        self.state = State.FULL_NAME
        self.file_id = ''
        self.school_info = ''

    def back_step(self) -> None:
        if self.state == State.SCHOOL_TYPE:
            self.state = State.SHIRAZI
            return

        back_index = BtiuUser.INFO_STATES.index(self.state) - 1
        self.state = BtiuUser.INFO_STATES[back_index]

    def next_step(self, jump: bool = False) -> None:
        next_index = BtiuUser.INFO_STATES.index(self.state) + 1 + jump
        self.state = BtiuUser.INFO_STATES[next_index]

    def say_info(self, message: str, bot: telepot.Bot) -> bool:
        if message == bl_back and self.state != State.FULL_NAME:
            self.back_step()
            return True

        elif self.state == State.FULL_NAME:
            self.full_name = message
            self.next_step()
            return True

        elif self.state == State.UNIVERSITY:
            self.university = message
            self.next_step()
            return True

        elif self.state == State.COMMITTEE:
            self.committee = message
            self.next_step()
            return True

        elif self.state == State.AGE:
            self.age = message
            self.next_step()
            return True

        elif self.state == State.PHONE_NUMBER:
            self.phone_number = message
            self.next_step()
            return True

        elif self.state == State.SHIRAZI:
            if message == bl_yes:
                self.next_step()
            elif message == bl_no:
                self.next_step(True)
            else:
                raise InputError('')

            return True

        elif self.state == State.SCHOOL_INFO:
            self.school_info = message
            self.next_step()
            return True

        elif self.state == State.SCHOOL_TYPE:
            if message in [bl_st_tiz, bl_st_dol, bl_st_ghe, bl_st_othr]:
                self.school_type = message
                self.next_step()
            else:
                raise InputError('')

            return True

        elif self.state == State.HOME_ADDR:
            self.home_addr = message
            self.next_step()
            return True

        elif self.state == State.HAVE_CAR:
            if message == bl_yes:
                self.has_car = True
            elif message == bl_no:
                self.has_car = False
            else:
                raise InputError('')

            self.next_step()
            return True

        elif self.state == State.KNOWN_SCHOOLS:
            self.known_schools = message
            self.next_step()
            return True

        elif self.state == State.FREE_TIMES:
            assert len(message.split('\n')) == 5
            self.free_times = message
            self.next_step()
            return True

        elif self.state == State.IDEA_AT_ALL:
            self.idea = message
            self.send_info(bot)
            self.state = State.MAIN_MENU
            return True

        elif self.state == State.PICTURE:
            bot.sendMessage(self.id, '')
            return False

        raise InputError('')

    def send_info(self, bot: telepot.Bot) -> None:
        info = info_template % (
            self.id, self.full_name, self.university, self.committee, self.age, self.phone_number, self.school_info,
            self.school_type, self.home_addr, self.has_car, self.known_schools, self.idea) + '\n\n' + self.free_times
        bot.sendMessage(self.id, info, 'Markdown')
        bot.sendDocument(self.id, self.file_id)
