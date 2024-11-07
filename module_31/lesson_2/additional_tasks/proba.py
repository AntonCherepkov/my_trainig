import re


# Цифра, окруженная не цифрами:
pattern_a = r'(?<!\d)\d(?!\d)'
print(re.findall(pattern_a, 'A2V3d45d6!'))

# Текст от #START# до #END#:
pattern_b = r'(?<=#START#).*?(?=#END#)'
print(re.findall(pattern_b, '#START#my big text#END#'))

# Цифра, после которой идёт ровно одно подчёркивание:
pattern_c = r'\d+(?=_(?!_))'
print(re.findall(pattern_c, '1__23_,'))

# Строка, в которой нет boo (то есть нет такого символа, перед которым стоит boo):
pattern_d = r'^(?:(?!boo).)*?$'
print(f'Первый поиск boo: {re.findall(pattern_d, "sdakfj__3 1!skaf")}')
print(f'Второй поиск boo: {re.findall(pattern_d, "фываbooasЗДЕСЬ НЕТ БУ")}')
