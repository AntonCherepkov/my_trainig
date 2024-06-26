print('Задача 6. Вредоносное ПО')
# Гера решил попрактиковаться в программировании и захотел написать небольшой скрипт, который после двух сообщений
# отправляет ещё одно на основе первых двух.
# Пользователь вводит две строки. В каждой из которой есть какое то количество специальных символов ! и ?. 
# Напишите программу, которая считает количество этих символов отдельно в первой строке и отдельно во второй
# строке. Если в первой строке их больше, чем во второй, то на экран выводится первая строчка, объедененная со 
# второй, а иначе вторая с превой. При равном количестве символов выводится "Ой!"

# Пример:
# Первое сообщение: Привет!
# Второе сообщение: Как дела? Что делаешь?
# Итоговое сообщение: Как дела? Что делаешь? Привет!
# 
# Первое сообщение: Хмм!!
# Второе сообщение: ?
# Итоговое сообщение: Хмм!!?  

def show_list(user_list):
    for elem in range(len(user_list)):
        print(f'{user_list[elem]}', end='')


count_first = 0
count_second = 0
first_list = []
second_list = []
result_list = []


first_message = input('Enter the first message: ')
second_message = input('Enter the second message: ')

first_list.extend(first_message)
second_list.extend(second_message)
if ((first_list.count('!') + first_list.count('?')) > 
        second_list.count('!') + second_list.count('?')):
    first_list.append(' ')
    first_list.extend(second_list)
    show_list(first_list)
elif ((first_list.count('!') + first_list.count('?')) < 
        second_list.count('!') + second_list.count('?')):
    second_list.append(' ')
    second_list.extend(first_list)
    show_list(second_list)
else:
    print('Ой')