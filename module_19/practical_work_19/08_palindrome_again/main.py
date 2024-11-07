cin_str = input('Введите строку: ')

counter_element = {
    element: sum(1 for elem in cin_str if elem == element)
    for element in cin_str
}

print(counter_element)

even_odd_element = {
    'number of even elements': sum(1 for count in counter_element.values() if count % 2 == 0),
    'number of odd elements': sum(1 for count in counter_element.values() if count % 2 != 0)
}

print(even_odd_element)

if even_odd_element['number of odd elements'] > 1:
    print('Нельзя сделать палиндром')
else:
    print('Можно сделать палиндром')

# зачет!
