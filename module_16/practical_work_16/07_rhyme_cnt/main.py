num_players = int(input('Enter the number of people: '))
step = int(input('Enter the number for the invoice: '))

list_players = []
list_players.extend(list(range(1, num_players + 1)))
begin_count = 0

while len(list_players) != 1:
    print(list_players)
    if begin_count > len(list_players) - 1:
        print(f'Starting an invoice with a number: {list_players[0]}')
    else:
        print(f'Starting an invoice with a number: {list_players[begin_count]}')
    end_count = (begin_count + step - 1) % len(list_players)
    print(f'The person under the number is eliminated: {list_players[end_count]}\n')
    list_players.pop(end_count)
    begin_count = end_count

print(f'there is still a person under the number: {list_players[0]}')

# зачет!
