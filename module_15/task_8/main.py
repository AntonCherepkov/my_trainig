print('Задача 2. Олимпиада')
# В олимпиаде по программированию участвует N человек, в списке участников они обозначаются номерами: 1, 2 и так
# далее до N. Эти участники поделены на команды по К человек.
# Напишите программу, которая принимает на вход количество участников и количество человек в каждой команде, а 
# затем генерирует список таких команд и выводит его на экран. 
# Обеспечте контроль ввода: в каждой команде должно быть ровно по К человек.
# Пример 1:
# Количество участников: 12
# Количество человек в команде: 4
# Общий список команды: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# Пример 2:
# Количество участников: 12
# Количество человек в команде: 5
# 12 участников невозможно поделить на команды по 5 человек!

num_part = int(input('Enter the number of participants: '))
print(f'The participants can be divided into ', end= '')
divider = []
teams_list = []

for i_num in range(2, num_part):
    if num_part % i_num == 0:
        divider.append(i_num)
    
if len(divider) == 0:
    print(f'{num_part} do not divided into at equal number of teams')
    num_teams = 0
else:
    while True:
        print(f'Enter the number of teams(you can only enter: {divider}):', end= ' ')
        num_teams = int(input())
        if num_part % num_teams == 0:
            break
        else:
            print('Are you dumb?')

count_parts = 1
for i_team in range(num_teams):
    teams_list.append(list(range(count_parts, count_parts + (num_part // num_teams) )))
    count_parts += num_part // num_teams

print(f'General list of teams: {teams_list}')
