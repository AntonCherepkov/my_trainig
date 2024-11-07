info_count = {
    1: 'Первый заказ',
    2: 'Второй заказ',
    3: 'Третий заказ',
    4: 'Четвертый заказ',
    5: 'Пятый заказ',
    6: 'Шестой заказ',
    7: 'Седьмой заказ',
    8: 'Восьмой заказ',
    9: 'Девятый заказ',
    10: 'Десятый заказ'
}

num_orders = int(input('Введите количество заказов: '))
orders_lists = []
result_dict = dict()

for i_order in range(1, num_orders + 1, 1):
    print(f'{info_count[i_order]}:', end=' ')
    cin_str = input('').split()
    orders_lists.append(cin_str)

# Тест на конкретных примерах:
# Первый заказ: Виталя мясная 1
# Второй заказ: Игорь бешамель 2
# Третий заказ: Виталя мясная 1
# Четвертый заказ: Игорь деревенская 3
# Пятый заказ: Игорь деревенская 2
# Шестой заказ: Ирина фридэй 2

for info_order in orders_lists:
    local_dict = dict()
    if info_order[0] in result_dict:
        if info_order[1] in result_dict[info_order[0]]:
            result_dict[info_order[0]][info_order[1]] += int(info_order[2])
        else:
            local_dict[info_order[1]] = int(info_order[2])
            result_dict[info_order[0]].update(local_dict)
    else:
        local_dict[info_order[1]] = int(info_order[2])
        result_dict[info_order[0]] = local_dict

for name, info in sorted(result_dict.items()):
    print(f'Заказы сделал - {name}')
    for pizza, num in info.items():
        print(f'Заказывал пиццу "{pizza}" - {num} шт.')
    print()

# зачет!
