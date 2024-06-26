print('Задача 1. Склады')
# У мебельного магазина есть два склада, на которых есть два склада, на которых хранятся разные категории товаров по парам 
# "название - количество".
# Магазин решил сократить аренду и скинуть все товары в большой склад (big_storage). После этого нас попросили реализовать 
# поиск по товарам.
# Напишите программу, которая объеденяет оба словаря в один (в bug_storage), а затем запрашивает у пользователя название товара
# и выводит на экран его количество. Если такого тавара нет, то выводит об этом ошибку. Для получения значения используйте
# метод .get().

def show_dict(user_dict):
    for elem in user_dict:
        print(f'{elem}: {user_dict[elem]}')


small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)
show_dict(big_storage)

search_product  = input('Enter the product name to search for: ')
if big_storage.get(search_product):
    print(f'{big_storage.get(search_product)} {search_product}')
else:
    print(f'There is no such product in stock')
