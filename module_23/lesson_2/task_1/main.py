import os

path_file = os.path.abspath(os.path.join(os.getcwd(), 'lesson_2', 'task_1', 'user_string.txt'))

user_file = None
try:
    user_str = input('Введите строку для записи в файл: ')
    user_file = open(path_file, 'w', encoding='utf-8')
    user_file.write(user_str)
except (FileNotFoundError, PermissionError) as error_one:
    print(error_one, ':\nНе получается открыть этот файл')
except ValueError as error_two:
    print(error_two, ':\nНе строка')
except Exception as error_three:
    print(error_three, ':\nОй, что то пошло не так!')
else:
    print('Файл записан!')
finally:
    if user_file and not user_file.closed:
        print('Закрываю файл!')
        user_file.close()
