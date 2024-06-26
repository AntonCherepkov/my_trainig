print('Задача 1. Результаты')
# Одному программисту дали задачу для обработки неких результатов тестирования двух групп людей. Файл первой 
# группы (group_1.txt) находится в папке task, файл второй группы (group_2.txt) - в папке Additional_info

# Содержимое файла group_1.txt:
# Бобровский Игорь 10
# Дронов Александр 20
# Жуков Виктор 35

# Содержимое файла group_2.txt:
# Павленко Геннадий 20
# Щербаков Владимир 35
# Marley Bob 30

# На экран нужно было вывести сумму очков первой группы, затем разность очков опять же первой группы и напоследок
# - произведение очков уже второй группы.
# Программист оказался не очень опытным, писал код наобум и даже не стал его проверять. И оказалось, этот код
# просто не работает. 
# Задача - исправить код горе программиста для решения поставленной задачи. Для проверки создайте необходимые 
# папки (task, Addition_info, Dont touch me) на своем диске в соответствии с картинкой и также добавте файлы 
# grorp_1.txt и group_2.txt

import os
path_group_1 = os.path.abspath(os.path.join('..', '..', 'task', 'group_1.txt'))
path_group_2 = os.path.abspath(os.path.join('..', '..', 'task', 'Addition_info', 'group_2.txt'))

summ = 0
diff = 0
one_file = open(path_group_1, 'r', encoding='cp1251')
for i_line in one_file:
    info = i_line.split()
    summ += int(info[2])
    diff -= int(info[2])

print('Сумма: ', summ)
print('Разность: ', diff)

compos = 1
two_file = open(path_group_2, 'r', encoding='cp1251')
for i_line in two_file:
    info = i_line.split()
    compos *= int(info[2])

print('Произведение: ', compos)

one_file.close()
two_file.close()
