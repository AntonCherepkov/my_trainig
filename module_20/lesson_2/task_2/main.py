print('Словари из списков')
# Создайте два списка, в каждом из которых лежит 10 случайных букв алфавита (могут повторяться). Затем для каждого
# списка создайте словарь из пар "индекс - значение" и выведете оба словаря на экран.

first_list = ['a', 's', 'd', 'f', 'd', 'f', 'a', 's', 'f', 'd', 'a', 's', 'f']
second_list = ['j', 'h', 'f', 'j', 'f', 'd', 'f', 'g', 's', 'a', 'g', 's', 'f']

first_dict = dict()
for index, symbol in enumerate(first_list):
    first_dict[index] = symbol

second_dict = dict()
for index, symbol in enumerate(second_list):
    second_dict[index] = symbol

print(first_dict)
print(second_dict)
