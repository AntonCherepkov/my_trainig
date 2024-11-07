import re


SERIAL_NUM = {
    1: 'первый',
    2: 'второй',
    3: 'третий',
    4: 'четвертый',
    5: 'пятый',
    6: 'шестой',
    7: 'седьмой'
}

pattern = r'\b[89]\d{9}\b'
numbers = [
    '9002005432',
    '9999999999',
    'x354234553',
    '234342234',
    '845345',
    '9343-543534'
]

is_number= re.compile(pattern)

for count, number in enumerate(numbers):
    print(f'Обрабатываю номер <{number}>:')
    if is_number.findall(number):
        print(f'{SERIAL_NUM[count + 1]} номер: всё в порядке\n')
    else:
        print(f'{SERIAL_NUM[count + 1]} номер: не подходит\n')
