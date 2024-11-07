site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}


def search_values(user_dict, search_key, count_depth=None):
    if search_key in user_dict:
        return user_dict[search_key]

    if count_depth == 0:
        return None

    result = None
    for key, value in user_dict.items():
        if isinstance(value, dict):
            result = search_values(value, search_key,
                                   count_depth - 1 if count_depth else None)
            if result:
                return result
    return result


user_key = input('Введите искомый ключ: ')

print('Хотите установить максимальную глубину вложенности?')
answer = input('Ответ [Y/N]: ').upper()
if answer == 'Y':
    nest_depth = int(input('Введите глубину вложенности: '))
    print('Значение ключа: ', search_values(site, user_key, nest_depth))
else:
    print('Значение ключа: ', search_values(site,user_key))

# зачет!
