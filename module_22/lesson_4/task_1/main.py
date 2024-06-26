print('Задание 1. Сумма чисел')
# Во входном файле number.txt записано N  целых чисел, каждое в отдельной строке. Напишите программу, которая выводит 
# их сумму в выходной файл answer.txt

import os
from random import randint

def count_lins(file_path):
    try:
        with open(file_path, 'r') as file:
            for i, _ in enumerate(file):
                pass
            else:
                return i + 1
    except FileNotFoundError:
        print('Файл не найден.')
        return 0
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return 0


in_file = open(os.path.join('doc', 'number.txt'), mode='w', encoding='utf-8')

num_lst = []
for _ in range(10):
    num_lst.append(str(randint(1, 10)))
str_num = '\n'.join(num_lst)
in_file.write(str_num)
in_file.close()

count_line = str(count_lins(os.path.join('doc', 'answer.txt'))+1)

out_file = open(os.path.join('doc', 'answer.txt'), mode='a+', encoding='utf-8')
in_file = open(os.path.join('doc', 'number.txt'), mode='r', encoding='utf-8')

summ = 0
for number in in_file:
    summ += int(number)

result_str = ' '.join([count_line, 'прогон, сумма чисел:', str(summ), '\n'])
print(result_str)
out_file.write(result_str)

in_file.close()
out_file.close()
