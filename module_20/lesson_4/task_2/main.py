print('Задача 2. Контакты 2')
# Мы уже реализовали телефонную книгу для Степана, однако её проблема была в том, что туда нельзя было добавить людей
# с одинаковыми именами. Надо это исправить.
# Напишите программу, которая запрашивает у пользователя имя контакта, фамилию и номер телефона, добавляет их в словарь
# и выводит на экран текущий словарь контактов. Словарь состоит из пар "Фамилия Имя : телефон", где "Фамилия Имя" - 
# составной ключ. Запрос на добавление идёт бесконечно (но можно задать своё условие для завершения программы). 
# Обеспечте контроль ввода: если этот человек уже в словаре, то выведете соответствующее сообщение.

def show_phonebook(my_dict):
    for info_name, number in my_dict.items():
        print(f'{info_name[0]} {info_name[1]} \t {number}')
    print()


phonebook = dict()

while True:
    name = input("Enter the person's name: ")
    surname = input("Enter the person's name: ")
    if (name, surname) in phonebook:
        print('The is such a person. Change the number?')
        choice = input('yes/no: ')
        if choice == 'yes':
            new_number = int(input('Enter the new namber: '))
            phonebook[(name, surname)] = new_number
        else:
            print()
            continue
    else:
        number_phone = int(input('Enter the phone number: '))
        phonebook[(name, surname)] = number_phone
    
    print(f'\nCurrent list:')
    show_phonebook(phonebook)

    if len(phonebook) == 3:
        break
