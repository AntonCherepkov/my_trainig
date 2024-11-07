import math


def is_prime(number_check):
    if number_check <= 1:
        return False
    if number_check == 2:
        return True
    if number_check % 2 == 0:
        return False
    for step in range(2, int(math.sqrt(number_check)) + 1):
        if number_check % step == 0:
            return False
    else:
        return True


def simple_index(user_data):
    return [num for index, num in enumerate(user_data) if is_prime(index)]


test_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(f'Значения, стоящие на позиции с индексом простого числа: {simple_index(test_list)}')

test_str = 'abcdefgh'
print(f'Значения, стоящие на позиции с индексом простого числа: {simple_index(test_str)}')

test_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
print(f'Значения, стоящие на позиции с индексом простого числа: {simple_index(test_tuple)}')

test_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
print(f'Значения, стоящие на позиции с индексом простого числа: {simple_index(test_dict)}')

# зачет!
