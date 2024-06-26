print('Задача 3. Удаление части')
# На вход в программу подаётся строка, состоящая из заглавных букв кириллицы. Напишите код, который проверяет
# каких букв в строке больше, прописных или заглавных. Если заглавных букв больше, то сделать все буквы строки
# заглавными, иначе сделать все прописными.
# Подсказка: используйте методы islower() и/или isupper().
# 
# Пример: 
# Введите строку: ПитоН - Это хорошО
# Результат: питон - это хорошо
# 
# Пример 2:
# Введите строку: ПиТоН - ЭтО УдоБНО
# Результат: ПИТОН - ЭТО УДОБНО

user_text = input('Enter the text: ')

# В решении задач под видео предлагают сковордякать два списка с малыми и большими буквами, и сравнить их
# длину:

low_letters = len([letter for letter in user_text if letter.islower()]) 
upp_letters = len([letter for letter in user_text if letter.isupper()])

if low_letters > upp_letters:
    user_text = user_text.lower()
elif low_letters < upp_letters:
    user_text = user_text.upper()
else:
    print('The number of characters of different case is equal to.')
print(user_text)
