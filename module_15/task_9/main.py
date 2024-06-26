print('Задача 3. Лавка')
# В небольшой фруктовой лавке у каждого фрукта есть название и цена. Эта информация хранится в одном большом
# списке, вот так:

goods = [['apple', 50], ['orange', 190], ['pear', 100], ['nectarine', 200], ['banane', 77]]

# Недавно в лавку привезли новый fruit_name по цене price, а после этого случилост ужасное: пвысили налоги, а
# значит повысились и цены на фрукты, на целых 8%!
# Напишите код, который добавляет в список goods ещё один список с новым фруктом и ценой(это запрашивается у 
# пользователя), а затем увеличивает цены всех фруктов на 8%

# Пример:
# Текущий ассортимент: [['apple', 50], ['orange', 190], ['pear', 100], ['nectarine', 200], ['banane', 77]]
# Новый фрукт: apicot
# Цена: 150
# Новый список с учетом нолога: [['apple', 54.0], ['orange', 205.2], ['pear', 108.0], ['nectarine', 216.0], 
# ['banane', 83.16], ['apicot', 162.0]]

print(f'Current list: {goods}')
new_fruit = input('Enter the new fruit: ')
price_new_fruit = int(input('Enter the price of new fruit: '))
list_fruit = []

list_fruit.append(new_fruit)
list_fruit.append(price_new_fruit)
goods.append(list_fruit)

print(f'New list: {goods}')

for i_fruit in goods:
    i_fruit[1] += i_fruit[1] / 100 * 8

print(f'Including tax: {goods}')
