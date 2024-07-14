class DivLessByMoreError(Exception):
    """Occurs when trying to divide a smaller number by a larger one"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
