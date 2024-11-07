# Функция, которая принимает одномерный массив, считает количество одинаковых элементов
# и возвращает в формате [[элемент_1, количество], [элемент_2, количество], ... [элемент_N, количество]]
# при этом все элементы нового массива упорядочены по индексу [0][N] и не повторяются
def sizing_sorting(user_list):
    buf_list = []
    result_list = []
    for elem in user_list:
        buf_list.append(elem)
        buf_list.append(user_list.count(elem))
        if result_list.count(buf_list) < 1:
            position = 0
            for i_num in result_list:
                if i_num[0] < buf_list[0]:
                    position = result_list.index(i_num) + 1
            result_list.insert(position, buf_list)
        buf_list = []

    return result_list


list_size = []
list_client = []
completed_request = 0

num_skates = int(input('Enter the number of skates: '))
for i_couple in range(num_skates):
    while True:
        print(f'Enter the size of the {i_couple + 1} pair:', end=' ')
        couple = int(input())
        if 57 > couple > 25:
            list_size.append(couple)
            break
        else:
            print('There is no such size')
print()

num_client = int(input('Enter the number of clients: '))
for i_client in range(num_client):
    print(f'Enter the shoe size of the {i_client + 1} customer:', end=' ')
    client = int(input())
    list_client.append(client)

list_size = sizing_sorting(list_size)
list_client = sizing_sorting(list_client)

for num_size in list_size:
    for num_client in list_client:
        if num_size[0] == num_client[0]:
            if num_size[1] > num_client[1]:
                completed_request += num_client[1]
            elif num_size[1] <= num_client[1]:
                completed_request += num_size[1]

print(f'They can take skates: {completed_request}')

# зачет!
