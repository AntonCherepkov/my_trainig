print('Задание 2. Поиск файла')
# В уроке мы написали функцию, которая ищет нужный нам файл во всех подкаталогах нужной нам директории. Однако, 
# как мы понимаем, файлов с таким названием может быть несколько.
# Напишите функцию, которая принимает на вход абсолютный путь до директории и имя файла, проходит по всем 
# вложенным файлам и папкам и выводит на экран все абсолютные пути с этим именем.

import os

def show_path(on_path, file_name, list_path = None):
    if list_path is None:                                       #Сделал запись в список всех найденных путей
        list_path = []

    for i_path in os.listdir(on_path):
        out_path = os.path.join(on_path, i_path)
        if i_path == file_name:
            list_path.append(out_path)
            return list_path
        elif os.path.isdir(out_path):
            result = show_path(out_path, file_name, list_path)
    else:
        return list_path

    return result


my_path = os.path.abspath(os.path.join('..'))
lst_path = show_path(my_path, 'task_2.py')

print('Список путей: ')
for i_path in lst_path:
    print(i_path)
        