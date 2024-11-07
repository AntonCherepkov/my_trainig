def sort_tuple(*input_tuple):
    for number_check in input_tuple:
        if not (isinstance(number_check, int)):
            return input_tuple

    work_list = list(input_tuple)

    for i_elem in range(0, len(input_tuple), 1):
        for j_elem in range(len(input_tuple) - 1, i_elem, -1):
            if work_list[i_elem] > work_list[j_elem]:
                work_list[i_elem], work_list[j_elem] = work_list[j_elem], work_list[i_elem]

    return tuple(work_list)


# print(sort_tuple(1, 6, 8, 8, 9, 5, 7, 5, 8, 0))

# зачет!
