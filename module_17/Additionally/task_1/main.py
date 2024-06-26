print('Задача: транспонирование строк')
# Транспорирование строк - это замена строк и колонок местами. Дан двумерный массив, при помощи вложенного генератора
# list comprehensions выполнить указанные изменения.

def show_list(user_list):
    for row in user_list:
        for col in row:
            print(col, end='\t')
        print()
    print('\n')

start_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(id(start_list))
show_list(start_list)

start_list = [[var[i] for var in start_list]for i in range(len(start_list[0]))]
print(id(start_list))
show_list(start_list)
