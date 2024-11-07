nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def open_list(user_list, result=None):
    if result is None:
        result = []
    for elem_list in user_list:
        if isinstance(elem_list, list):
            result = [
                i for elem in (result, open_list(elem_list))
                for i in elem
                ]
        else:
            result.append(elem_list)
    return result


print(nice_list)
print(open_list(nice_list))

# зачет!
