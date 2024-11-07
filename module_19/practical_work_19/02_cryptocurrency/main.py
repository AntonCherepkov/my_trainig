data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

print('Вывод ключей словаря:')
for my_keys in data.keys():
    print(my_keys, end=' ')
print()

print('\nВывод значений словаря:')
for my_val in data.values():
    print(my_val)

print('\ntask_2:')
data['ETH']['total_diff'] = 100

print('This is a test of the result:')
print(data['ETH']['total_diff'])

print('\ntask_3:')
data['tokens'][0]['fst_token_info']['name'] = 'doge'

print('This is a test of the result:')
print(data['tokens'][0]['fst_token_info'].get('name'))

print('\ntask_4:')
for list_tokens in data['tokens']:
    data['ETH']['total_out'] += list_tokens.pop('total_out')

    print('This is a test of the result:')
    print(data['ETH']['total_out'])
    for internal_dict in list_tokens:
        print(internal_dict, ': ', list_tokens[internal_dict])

print('\ntask_5:')
data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')

print('This is a test of the result:')
print(data['tokens'][1]['sec_token_info'].get('total_price'))
print(data['tokens'][1]['sec_token_info'].get('price'))

# зачет!
