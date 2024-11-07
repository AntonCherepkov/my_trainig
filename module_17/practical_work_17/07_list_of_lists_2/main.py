nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

print(nice_list)

# Применил вложенный цикл внутри конструкции list comrehensions
result_list = [q_num for i_num in nice_list
                     for j_num in i_num
                     for q_num in j_num]

print(result_list)

# зачет!
