import re


code = """
MyVar17 = OtherVar + YerAnother2Var
TheAnswerToLifeTheUniverseAndEverything, I = 42, 4
"""
print(f'Исходный код: {code}')

pattern = r'(?<!^)\w(?=[A-Z])'
updated_code = re.sub(pattern, lambda x: x.group() + '_', code).lower()
print(f'Переработанный код: {updated_code}')
