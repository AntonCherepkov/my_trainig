goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678'
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42}
],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520}
],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150}
],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97}
]
}


def product_sum_price_count(dict_code, dict_prod):
    return [
        (product, dict_info['quantity'] * dict_info['price'], dict_info['quantity'])
        for product, code in dict_code.items()
        for id_product, info in dict_prod.items() if code == id_product
        for dict_info in info
    ]


summ_price = product_sum_price_count(goods, store)

result_dict = {
    prod: [sum(price for prod_i, price, _ in summ_price if prod == prod_i),
    sum(count for prod_i, _, count in summ_price if prod == prod_i)]
    for prod, _, _ in summ_price
}

for name_product, info in result_dict.items():
    print('{:s} - {:d} штук, стоимость - {:d}'.format(
        name_product,
        info[1],
        info[0]
    ))
