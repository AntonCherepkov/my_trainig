import os
import random
from my_error import DivLessByMoreError


path_file = os.path.abspath(os.path.join('numbers.txt'))

with open(path_file, 'w', encoding='utf-8') as file_numbers:
    for _ in range(10):
        file_numbers.write(
            str(random.randint(1, 100))
            + ' '
            + str(random.randint(1, 100))
            + '\n'
        )

with open(path_file, 'r', encoding='utf-8') as file_numbers:
    for string in file_numbers.readlines():
        a, b = string.split()
        a, b = int(a), int(b)
        try:
            if a < b:
                raise DivLessByMoreError(f'Число {a} не должно быть больше числа {b}')
            else:
                result = round((a / b), 3)
                print(f'Результат деления {a} на {b} - {result}')

        except DivLessByMoreError as dlbme:
            print('Error: ', dlbme)
