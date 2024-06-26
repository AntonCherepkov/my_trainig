print('Задача 3. Неправильный код')
# Дан код, в котором должно происходить следующее: изначально есть кортеж из пяти чисел. Затем вызывается функция, 
# которая принимает на вход кортеж чисел, генерирует случайный индекс и генерирует случайное значение, а затем по
# этому индексу и значению меняет сам кортеж. Функция должна возвращать кортеж и случайное значение.
# В основном коде функция используется два раза, и на экран два раза выводится новый кортеж и случайное значение. 
# Причем второй раз выводится сумма первого случайного значения и второго.
# Однако код, который Вам дали, оказался нерабочим. Исправте его в соответствии с описанием.

import random

def update_tuple(user_tuple):
    rand_index = random.randint(0, len(user_tuple) - 1)
    rand_value = random.randint(0, 100)
    num_list = list(user_tuple)
    num_list[rand_index] = rand_value
    return tuple(num_list), rand_value


my_nums = 1, 2, 3, 4, 5
first_run, r_num_1 = update_tuple(my_nums)
print(first_run, r_num_1)
second_run, r_num_2 = update_tuple(first_run)
print(second_run, r_num_1 + r_num_2)
