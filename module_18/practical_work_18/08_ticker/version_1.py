# Первый способ решения задачи, сложность алгоритма неприлично большая О(2*n^2) = O(n^2)

str_1 = '01234567'
str_2 = '70123456'
count_shift = 0
is_exit = False

for i_pos in range(0, len(str_1), 1):
    if is_exit:
        break
    for j_pos in range(len(str_2), 0, -1):
        #        print(str_1[0:i_pos], '\t|', str_1[i_pos:len(str_1)], end='\t')
        #        print(str_2[0:j_pos], '\t|', str_2[j_pos:len(str_2)], end='\n')
        if str_1[0:i_pos] == str_2[j_pos:len(str_2)]:
            if str_1[i_pos:len(str_1)] == str_2[0:j_pos]:
                print(f'The second line is obtained from the first with a shift of {count_shift}')
                is_exit = True
                break
    count_shift += 1
else:
    print('The second line cannot be obtained from the first!')
