print('Задача 3. Удаление части')
# Дан список из N чисел, а также числа А и В (можно сгенерировать случайно, при этом А < В). Напишите программу,
# котрая удаляет элементы из списка с индексами от А до В. Не используйте дополнительные переменные и методы 
# списков.

from random import randint

num_a = int(input('Enter the first number: '))
num_b = int(input('Enter the second number: '))
len_list = int(input('Enter the length of the list: '))

if num_b < num_a:
    num_a, num_b = num_b, num_a

while num_b > len_list:
    print('The length of the list must be greater than the deletion boundury!')
    len_list = int(input('Enter it again: '))

list_num = [i_num for i_num in range(len_list)]

print(list_num)

list_num = list_num[:num_a] + list_num[num_b + 1:]

print(list_num)
