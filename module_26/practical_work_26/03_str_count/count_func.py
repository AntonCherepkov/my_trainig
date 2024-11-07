import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '02_files_path')))
from gen_func import gen_file_path
from typing import Generator


def is_start_comment(string: str) -> bool:
    """
    Function that determines whether a string is empty or a comment

    :param string: user string
    :type param: str
    :return: true or false
    :rtype: bool
    """
    if string.strip().startswith('#'):
        return False
    else:
        return True


def my_gen_count(path: str = os.path.join('..')) -> Generator[str, None, None]:
    """
    A function for counting lines in files with the extension "*.py" in the specified directory

    :param path: directory requested file python
    :type path: str
    :return: Generator[str, None, None]
    """

    my_exc = {'\n', ' '}
    count_string = 0

    for path_file in gen_file_path(path):
        if path_file.endswith('.py'):
            with open(file=path_file, mode='r', encoding='utf-8') as python_file:
                for string in python_file.readlines():
                    if not all(char in my_exc for char in string) and is_start_comment(string):
                        count_string += 1

            yield path_file, count_string
