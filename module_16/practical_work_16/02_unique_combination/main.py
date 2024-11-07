def merge_sorted_lists(list_1, list_2):
    result_list = []
    for i in list_1:
        result_list.append(i)
        for j in list_2:
            if not(result_list.count(j)):
                result_list.append(j)
                break
    return result_list


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)

# зачет!
