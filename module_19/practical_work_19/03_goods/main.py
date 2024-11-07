goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Это первый вариант исполнения программы

for product, code in goods.items():
    # print(f'{product} \t {code} ')
    for id_product, info in store.items():
        if code == id_product:
            # print(f'{id_product} \t {info}')
            price_var = 0
            summ_product = 0
            for dict_info in info:
                local_price = dict_info['price'] * dict_info['quantity']
                price_var += local_price
                summ_product += dict_info['quantity']

            print(f'Количество товара {product}: {summ_product}')
            print(f'Полная стоимость {product}: {price_var}')
            print()

# зачет!
