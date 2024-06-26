print('Задача 3. Поиск элемента')
# Когда мы работаем с большой многоуровневой структурой, нам нередко необходимо пройтись по ней и найти нужный
# элемент. Для этого в программировании используются специальные алгоритмы поиска.
# Напишите функцию, которая находит  заданный пользователем ключ в словарре и выдаёт значение этого ключа на 
# экран. В качестве примера можно использовать вот такой словарь:

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверно, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search_struct(struct, key):
    if key in struct:
        return struct[key]
     
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = search_struct(sub_struct, key)
            if result:
                break
    else:
        return None

    return result


search_key = 'body'

print(search_struct(site, search_key))
