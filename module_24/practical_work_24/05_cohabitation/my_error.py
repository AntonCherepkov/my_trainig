class ThreatLifeError(ValueError):
    """Occurs in the case of low well-being indicators"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        