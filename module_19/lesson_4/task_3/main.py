print('Задача 3. Различные цифры')
# Напишите программу, которая находит все различные цифры в символьной строке. Для решения используйте 
# множество (цифры будут различные, и поиск во множестве намного быстрее, чем в списке).
# Подсказка: можно использовать вот такое сравнение '0' <= x <= '9'

user_str = input('Enter the string: ')
user_str = set(user_str)

digit_in_str = ''.join({num for num in user_str if '0' <= num <= '9'})

print(digit_in_str)

print(''.join(user_str.intersection(set('0123456789'))))
