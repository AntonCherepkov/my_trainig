print('Задача 2. Поиск файла 2')
# Как мы помним - скрипты - это просто куча строк текста, хоть они и понятны только программисту. Таким образом 
# с ними можно работать точно так же, как и с обычными текстовыми файлами.
# Используя функцию поиска файла из предыдущего урока, реализуйте программу, которая находит внутри указанного 
# пути все файлы с искомым названием и выводит на экран текст одного из них (выбор можно сгенерировать случайно).
# Подсказка: можно сгенерировать список для сохранения найденного пути.

# Дополнительно: записать в файл все найденные пути, и путь файла, который вывели на экран.

import os
from random import randint

def show_path(on_path, file_name, list_path = None):
    if list_path is None:
        list_path = []

    for i_path in os.listdir(on_path):
        out = os.path.join(on_path, i_path)
        if i_path == file_name:
            list_path.append(out)
            return list_path
        elif os.path.isdir(out):
            result = show_path(out, file_name, list_path)
    else:
        return list_path

    return result


my_path = os.path.abspath(os.path.join('..'))
lst_path = show_path(my_path, 'task_2.py')

print('Список путей: ')
for i_path in lst_path:
    print(i_path)

if lst_path:
    selected_file = lst_path[randint(0, len(lst_path)-1)]
    print('\nОткрываю скрипт по адресу: ', selected_file, '\n')
    programmer_script = open(selected_file, 'r', encoding='utf-8')
    for i_line in programmer_script:
        print(i_line, end='')

    programmer_script.close()
else:
    selected_file = None
    print('\nФайлов с таким именем нет')



# Выполнение записи результатов в файл:

history_file = open('history_opened_and_search.txt', 'a', encoding='utf-8')
if lst_path:
    buf_str = '\n'.join(lst_path)
    history_file.write(
        'Список всех путей, содержащий файл:\n' + 
        buf_str +
        '\n\nПуть файла, который вывели на консоль:\n' +
        selected_file
    )
else:
    history_file.write('Программа не нашла заданного файла')

history_file.close()
