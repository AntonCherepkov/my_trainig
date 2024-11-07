from errors import *
from random import randint


class Carma:
    __all_carma = 500

    def __init__(self):
        self.current_carma = 0

    @classmethod
    def check_exception(cls):
        if randint(1, 10) == 1:
            accidental_exc = randint(1, 5)
            if accidental_exc == 1:
                return KillError('Персонаж кого то у**л!')
            elif accidental_exc == 2:
                return DrunkError('Персонаж с кем то напился!')
            elif accidental_exc == 3:
                return CarCrashError('Персонаж разбил авто!')
            elif accidental_exc == 4:
                return GluttonyError('Персонаж переел!')
            elif accidental_exc == 5:
                return DepressionError('Персонаж в депрессии!')
        else:
            return None

    def add_carma(self):
        add_carma = randint(1, 7)
        self.current_carma += add_carma

    def check_carma(self):
        exception = self.check_exception()
        if exception is None:
            if self.current_carma >= self.__all_carma:
                return True
            else:
                return False
        else:
            return exception
