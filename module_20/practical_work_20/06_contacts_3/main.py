phonebook = dict()


def add_contact():
    name_surname = tuple(input('Введите ФИ, через пробел: ').title().split())

    if name_surname in phonebook:
        print('Такой человек уже есть в справочнике!')
        print('Желаете изменить номер телефона?')
        change = input('[yes] - да: ')
        if change == 'yes':
            number_phone = int(input('Введите новый номер телефона: '))
            phonebook[name_surname] = number_phone
            return
        else:
            return

    number_phone = int(input('Введите номер телефона: '))
    phonebook[name_surname] = number_phone


def search_contact():
    surname = input('Введите фамилию: ').title()
    for name_surname, number in phonebook.items():
        if surname in name_surname:
            print('Имя: {}, Фамилия: {}, Телефон: {:d}'.format(
                *name_surname,
                number
            ))


def show_phonebook():
    for name, number in phonebook.items():
        print('Имя: {}, Фамилия: {}, Телефон: {:d}'.format(
            *name,
            number
        ))


while True:
    print('Чего желаете?\n'
          '[1] Добавить контакт\n'
          '[2] Найти контакт по фамилии\n'
          '[3] Ознакомится со всем справочником')

    user_choice = int(input('Выбор: '))
    if user_choice == 1:
        add_contact()
    elif user_choice == 2:
        search_contact()
    elif user_choice == 3:
        show_phonebook()
    else:
        print('Попробуйте ещё раз!')

# зачет!
