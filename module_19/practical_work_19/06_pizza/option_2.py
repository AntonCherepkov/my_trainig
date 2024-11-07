# Что бы не повторять два раза алгоритм ввода, сразу приводим список заказов в нужном формате
orders_lists = [
    ['Иванов', 'Пеперони', '1'],
    ['Петров', 'Де-Дюкс', '2'],
    ['Иванов', 'Мясная', '3'],
    ['Иванов', 'Мексиканская', '2'],
    ['Иванов', 'Пеперони', '2'],
    ['Петров', 'Интересная', '5']
]

result_dict = {
    surname[0]: {
        name_prod[1]:
            sum(int(num_prod[2]) for num_prod in orders_lists if num_prod[1] == name_prod[1])
        for name_prod in orders_lists if name_prod[0] == surname[0]
    }
    for surname in orders_lists
}

for name, info in sorted(result_dict.items()):
    print(f'Заказы сделал - {name}')
    for pizza, num in info.items():
        print(f'Заказывал пиццу "{pizza}" - {num} шт.')
    print()
