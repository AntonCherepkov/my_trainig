class AllErrors(Exception):
    """The base class of exceptions"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class KillError(AllErrors):
    """Occurs when a character kills"""
    pass


class DrunkError(AllErrors):
    """Occurs when a character gets drunk"""
    pass


class CarCrashError(AllErrors):
    """Occurs when a character crashes a car"""
    pass


class GluttonyError(AllErrors):
    """Occurs when a character has eaten too much"""
    pass


class DepressionError(AllErrors):
    """Occurs when a character is depressed"""
    pass
