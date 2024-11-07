def my_zip(first_data, second_data):
    return (
        (i_elem, j_elem) for i, i_elem in enumerate(first_data)
                         for j, j_elem in enumerate(second_data) if i == j
    )


def show_data(user_data):
    print(user_data)
    for elem in user_data:
        print(elem, end='')
    print()


test_list = [1, 2, 3, 4]
test_tuple = (5, 6, 7, 8)
test_set = {9, 10, 11, 12}
test_dict = {"a": 13, "b": 14, "c": 15, "d": 16}

result_1 = my_zip(test_list, test_dict)
result_2 = my_zip(test_list, test_list)
result_3 = my_zip(test_tuple, test_tuple)
result_4 = my_zip(test_set, test_list)

show_data(result_1)
show_data(result_2)
show_data(result_3)
show_data(result_4)

# зачет!
