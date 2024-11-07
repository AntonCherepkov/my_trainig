students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)

def interests_len_surname(info_dict):
    intersts_list = [
        one_interest for info_student in info_dict.values()
        for key_info, interests in info_student.items() if key_info == 'interests'
        for one_interest in interests
    ]

    len_all_surname = sum(len(surname) for info_student in info_dict.values()
                          for key_info, surname in info_student.items() if key_info == 'surname')

    return intersts_list, len_all_surname


id_age_list = [
    (id, age) for id, info_student in students.items()
    for key_info, age in info_student.items() if key_info == 'age'
]

list_interests, len_all_surname = interests_len_surname(students)

print(f'Список пар "ID студента - возраст": {id_age_list}')
print(f'Полный список инетресов всех студентов:\n{list_interests}')
print(f'Общая длинна всех фамилий студентов: {len_all_surname}')

# зачет!
