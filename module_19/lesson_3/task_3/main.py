# Это идея из готовых ответов, как всегда автор может удивлять.

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

# Вспомогательные структуры для корректного вывода

help_dict = {
    'rest': 'отдыхают',
    'training': 'тренеруются',
    'travel': 'путешествуют'  
}

team_list = ['A', 'B', 'C']
i_team = 0

for state in help_dict:
    print('Люди из команды {:s}, которые {:s}:'.format(
            team_list[i_team],
            help_dict[state]
        ))
    for _, player in players_dict.items():
        if player['team'] == team_list[i_team] and state == player['status']:
            print(player['name'], end=' ')
    print()
    i_team += 1
