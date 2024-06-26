print('Задача 2. Сервер')
# У вас есть данные о сервере, которые хранятся в виде словаря. Напишите программу, которая выводит для пользователя
# эти данные так же красиво, как они представленны в словаре:
# 

server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for config, info in server_data.items():
    print(f'{config}:')
    for setting, condition in info.items():
        print(f'    {setting}: {condition}')
