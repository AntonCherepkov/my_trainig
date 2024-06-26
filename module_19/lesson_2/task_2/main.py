print('Задача 2. Кризис фруктов')
# Мы работаем в одной небольшой торговой компании, где все данные о продажах фруктов за год сохранены в словаре в виде пар "Название
# фрукта - доход".
# В компании наступил небольшой кризис, и нам поручено провести небольшой анализ дохода. 
# Напишите программу, которая находит наибольший доход, затем выводит фрукт с минимальным доходом и удаляет его из словаря. Выведете
# итоговый словарь на экран. 
# 
# Результат работы программы:
# Общий доход компании за год составил  35419.34 рублей
# Самый маленький доход у gpapefruit. Он составляет 300.4 рублей
# Итоговый словарь: 
# apple - 5600.2 
# orange - 3500.45
# banana - 5000.0
# bergamot - 3700.56
# durian - 5987.23
# peach - 10000.5
# pear - 1020.0
# persimmon - 310.0  

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00
}

print("The company's total revenue for the year was: {}".format(
    sum(incomes.values())
))

for fruit in incomes:
    if incomes[fruit] == min(incomes.values()):
        print(f'The fruit {fruit} has a minimum income: {incomes[fruit]}')
        bad_fruit = fruit
incomes.pop(bad_fruit)

print('The final dictiinary:')
for fruit in incomes:
    print(f'{fruit} - {incomes[fruit]}')
