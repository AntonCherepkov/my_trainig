from typing import Generator
import os


def gen_file_path(
        path: str = os.path.abspath(os.path.join('..')),
        key: str = ''
) -> Generator[str, None, None]:
    """
    Generates full paths to files in the specified directory

    :param path: the absolute path of the directory to search for
    :type path: str
    :default path: the current directory with a step back
    :param key: the keyword for selection a subdirectory
    :type key: str
    :default key: all subdirectory in the specified directory
    :return: generator of full paths
    :rtype: Generator[str, None, None]
    """

    for dirpath, _, filename in os.walk(os.path.abspath(os.path.join('..'))):
        if key in dirpath:
            for file_name in filename:
                yield f'{dirpath}\\{file_name}'
