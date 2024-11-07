guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
concierge_var = ''

while True:
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    print(f'Гость пришёл или ушёл?', end= ' ')
    concierge_var = input()
    if concierge_var == 'пришёл':
        guest = input('Имя гостя: ')
        if len(guests) < 6:
            guests.append(guest)
        else:
            print(f'Прости, {guest}, мест нет')
    elif concierge_var == 'ушёл':
        guest = input('Имя гостя: ')
        if guests.count(guest) > 0:
            guests.remove(guest)
        else:
            print('Такого гостя не было')
    elif concierge_var == 'Пора спать':
        print('Вечеринка закончилась')
        break

# зачет!
