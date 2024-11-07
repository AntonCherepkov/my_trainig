def compere_list(user_list_1, user_list_2):
    if user_list_1 == user_list_2[::-1]:
        return True
    return False


seq_list = []
result_list = []
num_seq = int(input('Введите количество чисел в последовательности: '))

for _ in range(num_seq):
    num = int(input('Введите число: '))
    seq_list.append(num)

print(f'\nПоследовательность: {seq_list}')

while True:
    left_half = []
    right_half = []

    if len(seq_list) % 2 != 0:
        border = (len(seq_list) - 1) // 2
    elif len(seq_list) % 2 == 0:
        border = len(seq_list) // 2

    for i_left in range(0, border, 1):
        left_half.append(seq_list[i_left])
    if len(seq_list) % 2 != 0:
        border += 1
    for i_right in range(border, len(seq_list), 1):
        right_half.append(seq_list[i_right])

    if compere_list(left_half, right_half):
        break
    else:
        result_list.insert(0, seq_list[0])
        seq_list.pop(0)

print(f'Количество символов необходимо добавить: {len(result_list)}')
print(f'Символы: {result_list}')

# зачет!
