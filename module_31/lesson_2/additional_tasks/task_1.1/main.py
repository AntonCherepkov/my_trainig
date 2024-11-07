import re

text = 'Он --- серо-буро-малиновая редиска!!\n>>>:->\nА не кот.\nwww.kot.ru'

print(len(re.findall(r'\b[a-zA-Zа-яА-я-]+', text)))
