class CellNumberError(IndexError):
    """it is generated when the injected cell cannot be idenified"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
