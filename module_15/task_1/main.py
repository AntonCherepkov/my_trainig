print('Задача 1. Зоопарк')
# В маленьком зоопарке каждое животное сидит в отдельной клетке, всего этих животных несколько: лев, кенгуру, слон и
# обезъяна. В базе данных они храняться ввиде вот такого списка:
# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
# Сегодня в зоопарке завезли медведя (bear) и посадили его между львом и кенгуру. В итоге животных стало пять. А через
# неделю слона перевезли в другое место и в списке стало снова четверо животных.
# Реализуйте эти действия в коде программы и выведете в консоль итоговый список животных, а также посмотрите, в какой 
# клетке сидит лев и обезъяна. Для этого используйте методы списков.

# Результаты работы программы:
# Зоопарк: ['lion', 'bear', 'kangaroo', 'monkey']
# Лев сидит в клетке номер 1
# Обезъяна сидит в клетке номер 4

zoo = ['lion', 'kanraroo', 'elephant', 'monkey']
zoo.insert(1, 'bear')
zoo.remove('elephant')
print(f'Zoo: {zoo}')
i_mankey = zoo.index('monkey')
print(f'The {zoo[i_mankey]} is sitting in cage number {i_mankey + 1}')
i_lion = zoo.index('lion')
print(f'The {zoo[i_lion]} is sitting in cage number {i_lion + 1}')