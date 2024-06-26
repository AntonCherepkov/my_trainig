print('Задача 2. Путь к файлу')
# Все данные сайта лежат в одном проекте.  При написании кода, внутри этого проекта часто используется абсолютные 
# пути файлов, которые необходимо проверять.
# Пользователь вводит абсолютный путь к текстовому файлу, а также проверяемые данные: диск и расширение файла. 
# Напишите программу, которая корректность этого пути.
# 
# Пример:
# Путь к файлу: C:/user/docs/folder/new_file.txt
# На коком диске лежит файл: C
# Требуемое расширение файла: .txt
# Путь корректен!

path = '{disk}:/user/docs/folder/new_file.{expension}' 


user_disk = input('Enter the disk: ')
expension_file = input('Specify the expension: ')

path = path.format(
    disk=user_disk,
    expension=expension_file
)

if not path.endswith(expension_file):
    print('The file extensions is not correct')
elif not path.startswith(user_disk):
    print('Invalid disk is specified')
else:
    print('The file path is correct')
