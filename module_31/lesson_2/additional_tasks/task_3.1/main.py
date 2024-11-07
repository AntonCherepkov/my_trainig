import re


text = 'Московский государственный институт междунородных отношений'

pattern = r'(?:\b\w)+'
print(''.join(re.findall(pattern, text)).upper())

text = """микоян авиацию снабдил алкоголем,
народ доволен работой авиаконструктора
"""

print(''.join(re.findall(pattern, text)).upper())
