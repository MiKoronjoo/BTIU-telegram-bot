import enum


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

    def goToMain(self):
        self.state = State.MAIN_MENU
