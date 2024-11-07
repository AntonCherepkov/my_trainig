class AgeError(ValueError):
    """Исключение для детей старше родителей"""
    def __init__(self, message):
        self.message = message
        super().__init__(self, message)
