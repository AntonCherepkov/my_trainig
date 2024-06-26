print('Задача 2. Всё в одном')
# Ваш друг, который тоже проходит курс Python Basic, поехал с ноутбуком в другой город, и 
# там у него случилась беда: его диск пришлост отформатировать, а доступ в интернет 
# отсутствует. Остался только телефон с мобильным интернетом. Так как со связью и (с памятью)
# проблемы, друг попросил Вас скинуть файлом все решения и скрипты, которые у Вас сейчас есть.
# Напишите программу, которая копирует код каждого скрипта в папке проекта pyton_basic в 
# файл scripts.txt, разделяя код строкой из 40 символов "*".

import os
import glob

def list_path_scripts(root_dir, name_file='*.py', list_files=None):
    if list_files is None:
        list_files = []

    for i_dir in glob.glob(os.path.join(root_dir, '**', name_file), recursive=True):
        list_files.append(i_dir)
    
    return list_files


my_path = os.path.abspath(os.getcwd())
path_list = list_path_scripts(my_path)

out_file = open(os.path.join(my_path, 'doc', 'scripts.txt'), 'a+', encoding='utf-8')
for i_path in path_list:
    in_file = open(i_path, 'r', encoding='utf-8')
    for i_line in in_file:
        out_file.write(i_line)
    out_file.write('\n' + '*' * 40 + '\n')
    in_file.close()

out_file.close()
