print('Задача 3 для самостоятельного изучения')
# Дана строка из случайной последовательности чисел от 0 до 9. 
# Требуется создать словарь, который в качестве ключей будет принимать данные числа (т.е. ключи будут типом int), а в качестве
# значений - количество этих чисел в имеющейся последовательности. Для построения словаря создайте функцию count_it(sequence),
# принимающую строку из цифр. Функция должна возвращать словарь из 3-х самых частовстречающихся чисел.

import random

def count_it(my_str):
    buf_dict = {int(digit): my_str.count(digit) for digit in my_str}
    print(buf_dict)
    # Здесь надо конечно побольше знаний в целом и потом изучить работу функции sorted()
    res_list = sorted(buf_dict.items(), key=lambda element: element[1])
    print(res_list)
    return res_list[-3:]


user_str = ''
for _ in range(25):
    var_digit = str(random.randint(0, 9))
    user_str += var_digit

print(user_str)
print(count_it(user_str))
