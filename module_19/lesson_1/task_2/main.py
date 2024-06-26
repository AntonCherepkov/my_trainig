print('Задача 2. Студент')
# Пользователь вводит фамилию, имя студента, город его месторождения, вуз, в котором он учился, и все его оценки. Всё вводится в
# одну строку через пробел. Напишите программу, которая по этой информации составит словарь и выведет его на экран.
# 
# Пример:
# Введите информацию о студеднте через прбел
# (имя, фамилия, город, место учёбы, оценки): Илья Иванов Москва МГУ 4 5 5 3 4
# 
# Результат:
# Имя - Илья
# Фамилия - Иванов
# Город - Москва
# Место учёбы - МГУ
# Оценки - [4, 5, 5, 3, 4]

str_info = input('Enter the information about the student separated by a space\n'
                 'name, surname, sity, educational institution, grades: ')
list_info = str_info.split()
student_info = dict()

student_info['Name'] = list_info[0]
student_info['Surname'] = list_info[1]
student_info['Sity'] = list_info[2]
student_info['University'] = list_info[3]
student_info['Grade'] = []

for grade in list_info[4:]:
    student_info['Grade'].append(grade)

for key in student_info:
    print('{} - {}'.format(key, student_info[key]))
