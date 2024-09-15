from os import path
from random import randint


def gen_text():
    gen_str = ''
    for _ in range(10):
        for _ in range(10):
            gen_str += str(randint(0, 10)) + ' '
        gen_str += '\n'
    
    return gen_str


def gen_numbers(address_file):
    with open(address_file, 'r', encoding='utf-8') as file_obj:
        for string in file_obj.readlines():
            for symbol in string.split(' '):
                if symbol.isdigit():
                    yield int(symbol)


with open(path.join('numbers.txt'), 'w', encoding='utf-8') as number_file:
    number_file.write(
        gen_text()
    )

gen_obj = gen_numbers(path.join('numbers.txt'))
summ = sum(gen_obj)
print(summ)
