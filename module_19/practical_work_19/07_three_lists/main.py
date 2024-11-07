array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# print('Поиск элементов, которые есть в каждом '
#       'списке, без использования множеств')

counter_element = {
    element: sum(1 for i_arr in (array_1, array_2, array_3)
                   for i_elem in i_arr if element == i_elem)
    for array in (array_1, array_2, array_3)
    for element in array
}

print('Числа, которые есть в каждом массиве (без множеств):', end=' ')
for element, count in counter_element.items():
    if count == 3:
        print(f'{element}', end=' ')
print()

# print('Поиск элементов, которые есть в каждом '
#       'списке, с использованием множеств')

arr_set_1 = set(array_1[::])
arr_set_2 = set(array_2[::])
arr_set_3 = set(array_3[::])

print('Числа, которые есть в каждом массиве (со множествами):', end=' ')
for element in sorted(arr_set_1 & arr_set_2 & arr_set_3):
    print(element, end=' ')
print()

# print('Поиск элементов из 1-ого списка, которых нет '
#       'в других списках, без использования множеств')

list_uniq_nums = [
    uniq_num for uniq_num in array_1 if uniq_num not in
    [extra_elem for sum_arr in (array_2, array_3)
                for extra_elem in sum_arr]
]

print('Числа, которые есть в первом массиве, и нет в остальных '
      '(без множеств):', end=' ')
for element in list_uniq_nums:
    print(element, end=' ')
print()

# print('Поиск элементов из 1-ого списка, которых нет '
#       'в других списках, без использования множеств')

print('Числа, которые есть в первом массиве, и нет в остальных'
      '(со множествами):', end=' ')
for element in sorted(arr_set_1 - arr_set_2 - arr_set_3):
    print(element, end=' ')

# зачет!
