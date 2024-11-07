import re

text = """
Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова.
Смешно, не не правда ли? Не нужно портить хор хоровод.
"""

pattern = r'\b(\w+)([.,!?;:]*)\b(?:\s+\1\2\b)+'

update_text = re.sub(pattern, lambda x: x.group(1), text)
print(f'Новый текст: {update_text}')
