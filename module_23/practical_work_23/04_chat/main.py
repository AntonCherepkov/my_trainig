import os


def show_users(dict_users):
    for i_id, nickname in dict_users.items():
        print(nickname, ' [', i_id, ']')


def write_message(users_dict, chat):
    with open(chat, 'a', encoding='utf-8') as chat_file:
        count_enter_text = 1
        while count_enter_text:
            print('От имени какого участника добавить сообщение?')
            show_users(users_dict)
            id_user = int(input('>> '))
            if id_user in users_dict:
                print(f'\nСообщение от пользователя {users_dict[id_user]}:')
                message = input('>> ')
                chat_file.write(
                    users_dict[id_user]
                    + ' >> '
                    + message
                    + '\n'
                )
                count_enter_text -= 1
            else:
                print('\n Пользователя с таким ID не существует!')


def add_users(num_users, chat, dict_id=None):
    if dict_id is None:
        dict_id = dict()
        count_name = 0
    else:
        count_name = len(dict_id)

    num_users += count_name
    with open(chat, 'a', encoding='utf-8') as chat_file:
        while num_users != count_name:
            nickname = input(f'Введите имя {count_name + 1} участника чата: ')
            try:
                if nickname == '':
                    raise ValueError('Ошибка: Необходимо ввести имя пользователя')
                chat_file.write(
                    20 * '#' + '\n'
                    + 'Пользователь '
                    + nickname
                    + ' присоединился к чату!'
                    '\n' + 20 * '#' + '\n'
                )
                count_name += 1
                dict_id[count_name] = nickname

            except ValueError as exc:
                print(exc)

    return dict_id


def del_users(users, chat):
    with open(chat, 'a', encoding='utf-8') as chat_file:
        while len(users):
            try:
                print('Какой пользователь покинет чат?')
                show_users(users)
                del_user = int(input('>> '))
                if not (del_user in users.keys()):
                    raise ValueError
                user_name = users[del_user]
                remaining_users = [user for num, user in users.items() if num != del_user]

                chat_file.write(20 * '#' + '\n')
                chat_file.write(user_name + ' покинул чат\n')
                chat_file.write(20 * '#' + '\n')

                return {
                    num + 1: user for num, user in enumerate(remaining_users)
                }

            except ValueError as exc:
                print('Вы ввели неверное ID пользователя!\n')
            except Exception as exc:
                print('Произошла ошибка: ', exc, '\n')


def print_history(path_file):
    with open(path_file, 'r', encoding='utf-8') as file_obj:
        print(20 * '_')
        for string in file_obj:
            print(string, end='')
        print(20 * '_', '\n')


def main_menu():
    try:
        path_file = os.path.abspath('chathistoty.txt')
        num_part = int(input('Какое количество участников добавить в чат: '))
        if num_part < 1:
            raise IndexError('Ошибка: В чате должен быть хотя бы один участник!')
        users = add_users(num_part, path_file)
        print()

        while True:
            print('Выберете вариант действий:\n'
                  'Написать сообщение [1]\n'
                  'Добавить к чату участников [2]\n'
                  'Удалить участника из чата [3]\n'
                  'Вывести на экран историю сообщений [4]\n'
                  'Просмотреть полный список участников чата [5]\n'
                  'Закрыть чат [6]'
                  )
            choice = int(input('>> '))
            print()

            try:

                if 1 > choice or choice > 6:
                    raise ValueError

                elif choice == 1:
                    write_message(users, path_file)
                    print()

                elif choice == 2:
                    num_part = int(input('Какое количество участников добавить в чат: '))
                    users = add_users(num_part, path_file, users)

                elif choice == 3:
                    users = del_users(users, path_file)

                elif choice == 4:
                    print_history(path_file)

                elif choice == 5:
                    print('\nВсе участники настоящего чата:')
                    show_users(users)
                    print()

                else:
                    print('\nЧат завершён!')
                    break

            except ValueError as exc:
                print('Попробуйте ещё раз!')

    except (ValueError, IndexError) as exc:
        print(exc)


main_menu()

# зачет!
