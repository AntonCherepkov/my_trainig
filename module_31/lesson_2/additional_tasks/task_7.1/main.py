import re


# text = 'Да он олень, а не заяц!'
# text = 'Да он олень, а не 4 заяц!'
# text = 'Да он олень, а не 4 5 заяц!'
text = 'Да он олень, а не 4 5 6 заяц!'

# pattern = r'олень(?<=олень)(?:\S+\s*){0,5}(?=заяц)заяц'
pattern = r'олень(?:\S+\s*){0,5}заяц'

result = re.findall(pattern, text)
print(result)
