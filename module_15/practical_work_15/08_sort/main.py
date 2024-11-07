# Я изучал такие виды сортировки на примере языка С++ как: сортировка пузырьком (bubble sort) (менее эффективная,
# но более простая в реализации) и быстрая сортировка (quick sort) (основанная на реализации рекурсмвной функции)
# Честно признаться быструю сортировку я пока не готов написать самостоятельно.

def bubble_sort(list_user):
    for i_left in range(len(list_user)):
        for i_right in range(len(list_user) - 1, 0, -1):
            if i_right < i_left:
                break
            elif list_user[i_left] > list_user[i_right]:
                list_user[i_left], list_user[i_right] = list_user[i_right], list_user[i_left]
    return list_user

list_number = [1, 34, -23, 15, -4, 23, -56]
print(f"The original list: {list_number}")
print(f"Sorted list: {bubble_sort(list_number)}")

# зачет!
