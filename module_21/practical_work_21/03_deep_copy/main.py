site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

from copy import deepcopy


# Бонусом функция для красивого вывода в консоль:
def print_struct_console(user_struct, count_shift=0):
    if isinstance(user_struct, list):
        for i_elem in range(len(user_struct)):
            print_struct_console(user_struct[i_elem], count_shift)
            print('_' * 45)
    elif isinstance(user_struct, dict):
        for show_key, value in user_struct.items():
            print(count_shift * " " + show_key + ': ')
            print_struct_console(value, count_shift + 4)
    else:
        print(count_shift * " " + user_struct)


def deep_copy(obj):
    if isinstance(obj, (int, float, str, bool)):
        return obj
    if isinstance(obj, list):
        return [deep_copy(var) for var in obj]
    if isinstance(obj, dict):
        return {
            key: deep_copy(var) for key, var in obj.items()
        }
    return deepcopy(obj)


def changing_struct(struct, product):
    for key, sub_struct in struct.items():
        if isinstance(sub_struct, dict):
            res_struct = changing_struct(sub_struct, product)
        elif isinstance(sub_struct, str):
            # Сначала подмену подстроки реализовал таким способом:
            #           ' '.join([new_word if word == 'телефон' or word == 'iPhone' else word
            #                     for word in struct.split(' ')])
            struct[key] = sub_struct.replace('телефон', product).replace('iphone', product)
    return struct


def creat_site(num, temp, lst_sites=None):
    if num < 1:
        return lst_sites
    if lst_sites is None:
        lst_sites = []

    name_prod = input('Введите новый товар: ')
    lst_sites.append(changing_struct(deep_copy(temp), name_prod))

    print_struct_console(lst_sites)
    return creat_site(num - 1, temp, lst_sites)

num_sites = int(input('Сколько сайтов: '))
result_struct = creat_site(num_sites, site)

# зачет!
