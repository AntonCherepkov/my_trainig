import os


def search_broken_address(in_str):
    try:
        info_list = in_str.split()
        if len(info_list) != 3:
            raise IndexError('Не достаточно данных!')

        elif not info_list[0].isalpha():
            raise NameError('Имя не корректно!')

        elif not ('.' in info_list[1] and
                  '@' in info_list[1]):
            raise SyntaxError('Формат @mail не верен!')

        elif 10 > int(info_list[2]) or int(info_list[2]) > 99:
            raise ValueError('Возраст не корректен!')

        else:
            return None

    except (IndexError, NameError, SyntaxError, ValueError) as exc:
        return exc


with open('registrations.txt', 'r', encoding='utf-8') as in_file, \
        open(os.path.join('log', 'registrations_bad.log'), 'w', encoding='utf-8') as bad_file, \
        open(os.path.join('log', 'registrations_good.log'), 'w', encoding='utf-8') as good_file:

    for info_str in in_file:
        info_str = info_str[:-1]
        struct_error = search_broken_address(info_str)
        if struct_error:
            bad_file.write(
                info_str
                + ' -> '
                + str(struct_error)
                +'\n'
            )
        else:
            good_file.write(
                info_str
                + '\n'
            )



# зачет!


