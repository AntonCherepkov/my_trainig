from typing import Generator


def gen_square(limit: int = 1) -> Generator[int, None, None]:
    """
    Generator function for squaring a sequence of numbers
    
    :param limit: maximum number of iteretion
    :type limit: int
    :return: generator of squares of sequence numbers
    :rtype: Generator[int, None, None] 
    """

    count = 0
    while count < limit:
        count += 1
        yield pow(count, 2)
