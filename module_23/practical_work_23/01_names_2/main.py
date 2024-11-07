sum_len = 0
number_str = 0
list_str = []

with open('people.txt', 'r', encoding='utf-8') as in_file:
    for word in in_file:
        try:
            number_str += 1
            if word.endswith('\n'):
                word = word.rstrip('\n')
            length_str = len(word)
            sum_len += length_str
            if length_str < 3:
                list_str.append(number_str)
                raise BaseException('Количество символов меньнее трёх')

        except (FileNotFoundError, PermissionError) as exc:
            print(type(exc), ': Не удалось открыть файл!')

        except BaseException as count_error:
            with open('error.log', 'a', encoding='utf-8') as log_file:
                log_file.write(
                    'В строке №'
                    + str(number_str)
                    + ' менее трех символов...'
                    + '\n'
                )

    print(f'Количество всех символов: {sum_len}')
    if list_str:
        for string in list_str:
            print(f'В строке №{string} менее трех символов')
    else:
        print('Коротких строк не обнаружено')

# зачет!
