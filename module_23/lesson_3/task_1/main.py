import os

path_file = os.path.abspath(os.path.join( 'lesson_3', 'task_1', 'people.txt'))
print('Путь к файлу:', path_file)
count_str = 0
sym_sum = 0

try:
    with open(path_file, 'r', encoding='utf-8') as opened_file:
        for string in opened_file:
            len_str = len(string)
            count_str += 1
            if string.endswith('\n'):
                len_str -= 1
            if len_str <= 3:
                raise BaseException('Имя {} содержит меннее 3 символов'.format(
                    count_str
                ))
            print(f'{string} -> {len_str}')
            sym_sum += len_str

except (FileNotFoundError, PermissionError) as exc:
    print(exc, ': Файл не может быть открыт!')
except BaseException as exc:
    print('Это имя не берется в расчёт!')
finally:
    print('Всего символов, без учета переносов и коротких имён: ', sym_sum)
