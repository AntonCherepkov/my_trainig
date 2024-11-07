shift = int(input('Number of shift: '))
list_num = [1, 2, 3, 4, 5]

print(list_num)
while shift != 0:
    for i_num in range(len(list_num), 0, -1):
        if i_num == len(list_num):
            buf_num = list_num[i_num - 1]
            list_num[i_num - 1] = list_num[i_num - 2]
        elif i_num - 1 != 0:
            list_num[i_num - 1] = list_num[i_num - 2]
        else:
            list_num[0] = buf_num
    shift -= 1
    print(f'{list_num}')

# зачет!
