print('Задача 2. Игроки')
# Есть готовый словарь игроков, у каждого игрока есть имя, команда, в которой он играет, а также его текущий статус, в котором 
# указано, отдыхает он (Rest), тренеруется (Training) или путешествует (Travel).
# Напишите программу, котрая выводит на экран следующие данные в разных строках:
# 1. Все члены команды А, которые отдыхают;
# 2. Все члены команды Б, которые тренеруются;
# 3. Все члены команды С, которые путешествуют.

players_dict = {
    1: {'name': 'Vania', 'team': 'A', 'status': 'rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'travel'}
}

team_a_rest = [
    info_val['name']
    for info_val in players_dict.values()
    if info_val['team'] == 'A' and info_val['status'] == 'rest'
]

team_b_training = [
    info_val['name']
    for info_val in players_dict.values()
    if info_val['team'] == 'B' and info_val['status'] == 'training'
]

team_c_travel = [
    info_val['name']
    for info_val in players_dict.values()
    if info_val['team'] == 'C' and info_val['status'] == 'travel'
]

print(f'В команде А, которые отдыхают: {team_a_rest}')
print(f'В команде В, которые тренеруются: {team_b_training}')
print(f'В команде С, которые путешествуют: {team_c_travel}')
