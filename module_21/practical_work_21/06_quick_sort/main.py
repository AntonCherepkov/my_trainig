def quick_sort(lst):
    sup_elem = lst[-1:]
    if len(lst) <= 1:
        return lst

    min_lst = [i for i in lst if i < sup_elem[0]]
    max_lst = [j for j in lst if j > sup_elem[0]]
    equal_lst = [q for q in lst if q == sup_elem[0]]

    res_1 = quick_sort(min_lst)
    res_2 = quick_sort(max_lst)

    return res_1 + equal_lst + res_2


my_lst = [5, 8, 9, 4, 2, 3, 9, 1, 8]
print(my_lst)
sorted_lst = quick_sort(my_lst)
print(sorted_lst)

# зачет!
