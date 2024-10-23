import re


text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
result = re.match(r'wo', text)
print(f'Поиск шаблона в начале строки: {result}')

result = re.search(r'wo', text)
print(f'Поиск первого вхождения по шаблону: {result}')

substr = result.group()
st_pos = result.start()
end_pos = result.end()

print('Содержимое найденной подстроки: {a}\nНачальная позиция: {b}\nКонечная позиция: {c}'.format(
    a=substr, b=st_pos, c=end_pos
))

result = re.findall(r'wo', text)
print(f'Все вхождения: {result}')

result = re.sub(r'wo', 'ЗАМЕНА', text)
print(f'Измененный текст: {result}')
