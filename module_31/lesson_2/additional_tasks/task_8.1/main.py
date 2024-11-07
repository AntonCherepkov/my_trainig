import re


text = """
12 мало
лучше 123
1234 почти
12354 хорошо
стало 123456
супер 1234567
"""

pattern = r'(?<=\d)(?=(\d{3})+(?!\d))'

def add_match(match):
    return ','

result = re.sub(pattern, add_match, text)
print(result)
