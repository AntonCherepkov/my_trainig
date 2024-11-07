from square_class import SquareIterClass
from square_func import gen_square


print('Решение задачи с применением класса-итератора:')
square_iter = SquareIterClass(10)
for val in square_iter:
    print(val, end=' ')

print('\nРешение задачи с применением функции-генератора:')
for val in gen_square(10):
    print(val, end=' ')

user_num: int = 10
print('\nРешение задачи с применением генераторного выражения:')
print(f'Число пользователя: {user_num}')
gen_exp = (pow(i, 2) for i in range(1, user_num + 1))
for num in gen_exp:
    print(num, end=' ')
