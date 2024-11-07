def reverse_out(list_user):
    num = len(list_user)
    for i_num in range(num - 1, -1, -1):
        if list_user[i_num] % 2 == 0:
            list_user.append(list_user[i_num])
    del list_user[0:num]
    return list_user


numbers_list = [-8, 9, 78, 56, 47, 69, 7, 8, 13]
print(f'{id(numbers_list)} -> {numbers_list}')
numbers_list = reverse_out(numbers_list)
print(f'{id(numbers_list)} -> {numbers_list}')

# зачет!
