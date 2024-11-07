class MatixDimensionError(ValueError):
    """
    Generated when the matrix is not square
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        