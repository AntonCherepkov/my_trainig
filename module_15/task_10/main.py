print('Задача про Анфису')
# Сообщите Анфисе кто ваши друзья

name_friend = ''
list_friend = []

while True:
    name_friend = input('Who is your friend? ')
    if name_friend == 'end':
        break
    else:
        list_friend.append(name_friend)

# Сделать на основе имеющегося списка вложенный список, с конструкцией: [[имя, город], ...] 

person = []
town = ''

for i_friend in range(len(list_friend)):
    print(f'Enter the town for {list_friend[i_friend]}')
    town = input()
    person.append(list_friend[i_friend])
    person.append(town)
    list_friend.insert(i_friend, person)
    list_friend.pop(i_friend + 1)
    person = []

print(list_friend)