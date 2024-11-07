from typing import Optional, Tuple


class Day:
    """
    Этот класс базовый для дня в дате
    
    Args:
        day (str): день
    """
    def __init__(self, day: str) -> None:
        self.day = day 

 
    def __str__(self) -> str:
        month_year_str = super().__str__()
        return f'День: {self.day}\t' + month_year_str


class Month:
    """
    Этот класс базовый для месяца в дате

    Args:
        month (str): месяц

    Attributes:
        MONTH_DICT (dict): словарь для определения месяца по порядковому номеру
    """
    MONTH_DICT = {
        1: 'январь',
        2: 'февраль',
        3: 'март',
        4: 'апрель',
        5: 'май',
        6: 'июнь',
        7: 'июль',
        8: 'август',
        9: 'сентябрь',
        10: 'октябрь',
        11: 'ноябрь',
        12: 'декабрь'
    }


    def __init__(self, month: str) -> None:
        self.month = month


    def __str__(self):
        year_str = super().__str__()
        return f'Месяц: {self.MONTH_DICT[int(self.month)]}\t' + year_str


class Year:
    """
    Этот класс базовый для года в дате
    
    Args:
        year (str): год    
    """
    def __init__(self, year: str) -> None:
        self.year = year

    
    def __str__(self):
        return f'Год: {self.year}'


class Date(Day, Month, Year):
    """
    Класс, описывающий всю дату целиком.
    Наследуется от классов 'Day', 'Month', 'Year' для обеспечения 
    удобной работы с датами.

    Args:
        string_date (str): входная строка даты в формате "DD-MM-YYYY"

    Attributes:
        day (str): день
        month (str): месяц
        year (str): год
        _string_date (str): сформированная из атрибутов day, month и year строка в формате "DD-MM-YYYY"

    Methods:
        split_date(): делит строку формата "DD-MM-YYYY" на кортеж формата ("DD", "MM", "YYYY")
        is_date_valid(): метод класса. Проверяет входящую строку на соответствие формату "DD-MM-YYYY"
        is_instance_date_valid(): на основе метода класса is_date_valid(), проверяет атрибут _string_date
            экземпляра на валидность
    """
    def __init__(self, string_date: str) -> None:
        self.split_date(string_date)
        self._string_date = string_date


    @property
    def string_date(self):
        """Возвращает строку экземпляра, содержащую дату"""
        return self._string_date

    @string_date.setter
    def string_date(self) -> str:
        """Изменяет строку экземпляра, содержащую дату"""
        self._string_date =  f'{self.day}-{self.month}-{self.year}'


    def split_date(self, in_date: str) -> Tuple[int, ...]:
        """
        Метод, разделяющий переданную строку в формате dd-mm-yyyy 
        на три отдельные составляющие: день, месяц, год

        args:
            string_date (str): входная строка с полной датой

        returns:
            (dd, mm, yyyy) (Tuple[int, ...]): кортеж с числом, месяцем, годом

        raises:
            TypeErrore: Некорректный формат даты!
        """
        if Date.is_date_valid(in_date):
            self.day, self.month, self.year = (date_elem for date_elem in in_date.split('-'))
        else:
            raise TypeError('Некорректный формат даты!')

    
    @classmethod
    def is_date_valid(cls, in_date: str) -> bool:
        """
        Метод - флаг, который проверяет переданную строку на корректность 
        оформления, и возвращает Тrue, если корректно и False если не корректно

        args:
            string_date (str): входная строка с полной датой

        returns:
            is_valid (bool): флаг корректности строки
        """
        if isinstance(in_date, str):
            if in_date.count('-') == 2:
                list_date = in_date.split('-')
                if (0 < int(list_date[0]) < 31 and
                        0 < int(list_date[1]) <= 12 and
                        len(list_date[2]) == 4):
                    
                    return True
        return False
    

    def is_instance_date_valid(self) -> bool:
        """
        Метод, адаптирующий метод класса проверки валидности строки для экземпляров.
        Может пригодиться при изменении непосредственно даты, месяца или года в уже 
        созданном экземпляре класса Date

        returns:
            is_valid (bool): валидность строки, в         
        """
        return self.__class__.is_date_valid(self.string_date)


second_date = Date('15-07-2024')
first_date = Date('16-07-2023')

print('Отдельно день: {day}\tОтдельно месяц: {month}\tОтдельно год: {year}'.format(
    day=first_date.day,
    month=first_date.month,
    year=first_date.year
))

print('Отдельно день: {day}\tОтдельно месяц: {month}\tОтдельно год: {year}'.format(
    day=second_date.day,
    month=second_date.month,
    year=second_date.year
))

print('\nВыводим все целиком, методом __str__():')
print(first_date)
print(second_date)

print('\nПроверка корректности, как в задании:')
print(f'Проверка валидности строки экземпляра: {first_date.is_instance_date_valid()}')
print(f'Проверка валидности строки: {Date.is_date_valid("16-12-2023")}')
