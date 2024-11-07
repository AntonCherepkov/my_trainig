from datetime import datetime
import re


class MyTime:
    """Класс для формирования даты и времени в заданном формате"""
    VALID_SYMBOLS = {'b': '%b', 'd': '%d', 'Y': '%Y', 'H': '%H', 'M': '%M', 'S': '%S'}
    VALID_FORMATS = ['%H:%M:%S - %b %d %Y', '%b %d %Y - %H:%M:%S']
    
    @classmethod
    def now(cls, user_format: str = 'H:M:S - b d Y') -> str:
        """
        Ключевой метод, принимает на вход шаблон времени пользователя,
        возвращает строку с датой и временем
        """
        format_time = cls.format_conversion(user_format)

        now_time = datetime.now()
        str_time = now_time.strftime(format_time)

        return str_time


    @classmethod
    def is_valid_symbol(cls, in_format: str) -> bool:
        symbols = re.split(r'[- :]', in_format)

        for symbol in symbols:
            if symbol not in cls.VALID_SYMBOLS:
                return False
            return True


    @classmethod
    def format_conversion(cls, i_format: str) -> str:
        if cls.is_valid_symbol(i_format):
            for key, value in cls.VALID_SYMBOLS.items():
                i_format = i_format.replace(key, value)
        
        if i_format not in cls.VALID_FORMATS:
            raise TypeError('Передан не корректный формат!')
        
        return i_format
