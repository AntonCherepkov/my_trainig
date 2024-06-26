print('Задача 2. Долги')
# Один наш друг занял у нас определенную сумму денег и всё никак не может её вернуть. А деньги нам нужны.
# Поэтому мы решили написать небольшой скрипт-напоминалку, который, возможно, разбудит его совесть.
# Напишите программу, которая получает на вход имя и долг, а затем выводит на экран сообщение, где имя 
# повторяется несколько раз (и долг, возможно, тоже). Используйте числа в названиях ключей.
# 
# Пример:
# Введите имя: Том
# Введите долг: 100
# Том! Том, привет! Как дела, Том? Где мои 100 рублей? Том!

name_friend = input('Enter the name: ')
amount_debt = input('Enter the debt: ')

message = '{name}! {name}, привет! Как дела, {name}? Где мои {debt} рублей? {name}!'.format(
    name = name_friend,
    debt = amount_debt
)

print(message)
