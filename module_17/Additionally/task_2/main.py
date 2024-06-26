print('Задача: Список в качестве итерируемого объекта')
# Сам по себе генератор списка поддерживает механизм итерирования - пребора элементов через итератор, поэтому может быть 
# использован в операторе for, например так:

master_list = [var ** 2 for var in [start + 1 for start in range(5)]] 
print(master_list)

double_list = [var ** 2 for var in range(1, 6)]
print(double_list)
