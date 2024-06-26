print('Задача 1. Создание кортежей')
# Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно. Также заполните второй кортеж числами
# от -5 до 0. Объедените два кортежа, создав тем самым третий кортеж. С помощью метода кортежа определите в нём 
# количество нулей. Выведете на экран третий кортеж и количества нулей в нем.

import random

one_tuple = list()
two_tuple = list()

for _ in range(10):
    one_tuple.append(random.randint(0, 5))
    two_tuple.append(random.randint(-5, 0))

print(one_tuple, two_tuple)

one_tuple = tuple(one_tuple)
two_tuple = tuple(two_tuple)

print(one_tuple, two_tuple)

print(one_tuple.count(0), two_tuple.count(0))

three_tuple = one_tuple + two_tuple

print(three_tuple)

print(three_tuple.count(0))
