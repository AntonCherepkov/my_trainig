print('Задача для самостоятельного изучения')
# Написать функцию to_dict(list), которая принимала бы аргумент в виде списка и возращала словарь, в котором каждый элемент
# списка является и ключом и значением. Предполагается, что элементы списка будут соответствовать правилам заданием ключей
# в словарях.

def to_dict_1(user_list):
    new_dict = dict()
    for elem in user_list:
        new_dict[elem] = elem
    return new_dict

# dict comprehension
def to_dict_2(user_list):
    return {elem: elem for elem in user_list}


my_list = [1, 2, 3, 4, 5]

print(to_dict_1(my_list))
print(to_dict_2(my_list))
