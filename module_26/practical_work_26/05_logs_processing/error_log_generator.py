import hashlib
from typing import Generator


def super_hash(in_str: str) -> int:
    """
    A function for hashing based on the "hashlib" module

    :param in_str: incoming hashing string
    :type in_str: str
    :return: the resulting hash value
    :rtype: int
    """
    return int(hashlib.sha256(in_str.encode('utf-8')).hexdigest(), 16)


def is_substring(text: str, pattern: str = 'ERROR') -> bool:
    """
    The function of searching for a substring useng the Rabbin-Karp method

    :param text: the full text in which we are searching
    :type text: str
    :param pattern: the substring to look for in the text (default is 'ERROR')
    :type pattern: str
    :return: found - True, is not found - False
    :rtype: bool
    """
    if not text or not pattern:
        return False

    pattern_hash = super_hash(pattern)
    window_hash = super_hash(text[:len(pattern)])
    coin = False

    for i in range(len(text) - len(pattern) + 1):
        if (pattern_hash == window_hash 
                and text[i:i + len(pattern)] == pattern):
            coin = True
            break
        window_hash = super_hash(text[i + 1:i + 1 + len(pattern)])
    
    return coin


def error_log_generator(path_file: str) -> Generator[str, None, None]:
    """
    The function generator for lazy evaluation

    :param path_file: path to log file
    :type path_file: str
    :return: error string
    :rtype: Generator[str, None, None]
    """
    with open(file=path_file, mode='r', encoding='utf-8') as open_file:
        for error_string in open_file.readlines():
            if is_substring(text=error_string):
                yield error_string
