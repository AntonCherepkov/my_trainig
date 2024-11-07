import re


text = """В         этом
предложении разрывы строки... Но это
не так важно!  Совсем?   Да, совсем! И это

не      должно мешать. 
"""

# Это тухлый способ решения с постепенным улучшением... Сделанный для прихода понимания:
# Сначала удаляем лишние пробелы из текста:
pattern_1 = r'(?:\s(?=\s+))'
up_text_1 = re.sub(pattern_1, '', text)
print(up_text_1)

# Потом удаляем не нужные переносы строк:
pattern_2 = r'\n'
up_text_2 = re.sub(pattern_2, ' ', up_text_1)
print(up_text_2)

print()

# Потом добавляем переносы строк в нужные места:
pattern_3 = r'(?<=[!?;.]).+?(?=[А-Я])'
up_text_3 = re.sub(pattern_3, lambda x: x.group() + '\n', up_text_2)
print(up_text_3)


# А вот крутой паттерн для решения задачи в один заход:
pattern = r'\s+(?=\s)|\n|[!.?;]\s(?!\.+)'
up_text_4 = re.sub(pattern, lambda x: x.group() + '\n' if x.group() in ['. ','! ', '? '] else ' ', text)
print('\nENTER THE COOL RESULT:\n')
print(up_text_4)