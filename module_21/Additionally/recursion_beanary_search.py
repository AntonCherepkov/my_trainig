print('Рекурсивный бинарный поиск. Моё исполнение')

def binary_search(list_nums, num_search, beg, end):
    if beg > end:
        return -1

    middle_index = round((beg + end) / 2)
    if num_search == list_nums[middle_index]:
        end_index = middle_index
        return end_index
    elif num_search > list_nums[middle_index]:
        beg = middle_index + 1
        return binary_search(list_nums, num_search, beg, end)
    elif num_search < list_nums[middle_index]:
        end = middle_index - 1
        return binary_search(list_nums, num_search, beg, end)


def binary_search_2(list_nums, num_search, beg, end):
    if beg > end:
        return -1
    mid = (beg + end) // 2
    if list_nums[mid] == num_search:
        return mid
    elif list_nums[mid] < num_search:
        return binary_search_2(list_nums, num_search, mid + 1, end)
    else:
        return binary_search_2(list_nums, num_search, beg, mid - 1)
    

search = 10
test_list = [2, 4, 5, 6, 8, 10, 14, 15, 16, 19, 20, 25]

result_1 = binary_search(test_list, search, 0, len(test_list)-1)

print(f'Искомый элемент находится по индексу: {result_1}')

print(f'\nВариант исполнения из учебника:')

result_2 = binary_search_2(test_list, search, 0, len(test_list)-1)

print(f'Искомый элемент находится по индесу: {result_2}')

print(f'\nПотому что абсолютно одинаково, все, только не знал как проверить отсутствие элемнета')
