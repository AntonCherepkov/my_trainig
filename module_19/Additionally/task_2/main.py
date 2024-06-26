print('Задача 2 из самостоятельного изучения')
# Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs), которая принимает
# неограниченное количество параметров "ключ: значение" и обновляет созданный им словарь my_dict, состоящий всего из одного
# элемента со значением "we can do it". Воссоздайте эту функцию.

my_dict = {'a': 'we can do it'}

def  biggest_dict(**kwargs):
    return my_dict.update(kwargs)


biggest_dict(b=1, c=2, d=3, e=4)
print(my_dict)

# the right decision
