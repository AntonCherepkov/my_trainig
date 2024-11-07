def sum_best(*number):
    result = 0
    for elem in number:
        if isinstance(elem, (int, float)):
            result += elem
        elif isinstance(elem, list):
            result += sum_best(*elem)
    return result

# first_lst = [1, 2, [3, [4]], 3, 6]
# second_lst = [[3, 5, [6]], 3, [3, 2]]
# third_lst = [3, 3, [2, 1, [5]], 4, 2]
#
# print(sum_best(first_lst))        #19
# print(sum_best(second_lst))       #22
# print(sum_best(0, 4, 3, 6, 7))    #20
# print(sum_best(2, 3, 4, 2, 1))    #12

# зачет!
