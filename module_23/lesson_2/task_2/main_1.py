def to_float(num_str):
    try:
        return float(str(num_str).replace(',', '.'))
    except ValueError as exc:
        print('Не может быть преобразовано в float')


test_list = [
    123.3, 
    321,
    213.34,
    'Anton',
    '234',
    '12,123'
    'nan',
    '1e-3'
]

for elem in test_list:
    print(to_float(elem))
