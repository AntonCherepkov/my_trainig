print('Задача 1. Заказ фруктов')
# Дан словарь, в котором содержится товар (фрукты): ключи - это названия фруктов, значения - необходимое количество килограммов.
# Этот словарь обозначает заказ товара. 
# И дан второй словарь, обозначающий наличие товара. Во втором словаре: ключ - это название товаров, а значение - цена за 
# килограмм. 
# 1. При помощи методов get() и установки значения по умолчанию проверьте, есть ли товар на складе, и получите его цену. Если 
# товара нет, то по умолчанию получите 0. Посчитайте итоговую выручку компании по имеющимся товарам.
# 2. Напишите программу, которая суммирует стоимость(цена * количество) всех заказанных товаров, и выведете итоговую сумму в 
# консоль.

order = {
    'apple': 2,
    'bannana': 3,
    'pear': 1,
    'watermelon': 10,
    'choclate': 5
} 

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'bannana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00
}

total_price = 0

for name_product in order.keys():
    if incomes.get(name_product, 0):
        print('There is {name} in stock'.format(
            name = name_product), end=' ')
        price = incomes[name_product] * order[name_product]
        print('The price for {:d} kg {:s} {:.2f} rubles'.format(
            order[name_product],
            name_product,
            price
        ))
        total_price += price

print(f'The result price = {total_price}')
