print('Задача 3. Контакты')
# Энтузиаст Степан, купив новый телефон, решил написать для него свою собственную операционную систему. И, конечно же, превое, 
# что он захотел в ней реализовать, - это телефонная книга.
# Напишите программу, которая запрашивает у пользователя Имя контакта и номер телефона, добавляет их в словарь и выводит на экран
# текущий словарь контактов. Запрос на добавление идёт бесконечно (но можно задать своё условие для завершения программы). Обес-
# печте контроль ввода информации: если это имя уже есть в словаре, то выведете соответствующее сообщение.
# 
# Пример:
# Текущие контакты на телефоне:
# <Пусто>

# Введите имя: Иван
# Введите номер телефона: 89009009090
# 
# Текущие контакты на телефоне:
# Иван 89009009090
# 
# Введите имя: Лена
# Введите номер телефона: 89008008080
# 
# Текущие контакты на телефоне:
# Иван 89009009090
# Лена 89008008080
# 
# Введите имя: Иван
# Ошибка! Такое имя уже существует

def show_dict(my_dict):
    print('Current contact list:')
    if not(len(my_dict)):
        print('<empty>')
    else:
        for name in my_dict:
            print('{} {}'.format(
                name,
                my_dict[name]
            ))
    print()


phonbook = dict()
num_add, num_contacts = 0, 1

while len(phonbook) != num_contacts:
    show_dict(phonbook)

    name = input('Enter the name: ')
    if name in phonbook:
        print('Error: this name is in the contacts')
    else:
        phone_num = input('Enter the phone number: ')
        phonbook[name] = phone_num
    print()
    
    if num_add + num_contacts == len(phonbook):
        num_add = int(input('How many contacts will we add? '))
        num_contacts += num_add

show_dict(phonbook)

# PS: Я реализавал выход из программы дополнительным вопросом: "Сколько добавить контактов ещё"