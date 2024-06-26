print('Задача 1. Анализ цен')
# Нашему другу заказали написать программу, которая анализирует цены на бирже. Она получает этот пакет данных
# но делать что либо с ним нельзя. Для нормальной работы аналитической программы берется новый список, который
# равен тому, что пришло. Затем идёт работа с новым списком: если есть отрицательные цены, то программа их 
# зануляет и в конце работы программы выводит их на экран, сколько денег мы по итогу потеряли.
# Дополнительно: сделать так, чтобы список цен генерировался случайно (диапазон можно выбрать любой).

from random import randint

prices_stock_exchenge  = [randint(-50, 100) for _ in range(15)]

summ = 0
new_list_prices = prices_stock_exchenge[::]     #Можно копирнуть: new_list_prices = prices_stock_exchenge.copy()

for elem in new_list_prices:
    if elem < 0:
        summ += abs(elem) 
new_list_prices = [new_list_prices[i_elem] if new_list_prices[i_elem] > 0 
                   else 0 for i_elem in range(len(new_list_prices))]

print(prices_stock_exchenge)
print(new_list_prices)
print(summ)