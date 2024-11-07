# Это третий способ решения. Он как и предыдущий имеет сложность О(n). Разница с предыдущим - применение методов startswith и
# endswith, что должно давать выигрыш по скорости (но это не точно) и делает код более читаемым (но это не точно)

while True:
    us_str_1 = input('The first string: ')
    us_str_2 = input('The second string: ')
    if len(us_str_1) == len(us_str_2):
        break
    else:
        print('Cheking makes sense if the rows are equal!')
count_shift = 0

for i in range(1, len(us_str_1), 1):
    if us_str_1.endswith(us_str_2[0:i]):
        if us_str_1.startswith(us_str_2[(len(us_str_2) - i - 1):len(us_str_2)]):
            print(f'The second line is obtained from the first with a shift of {count_shift}')
            break
        else:
            print('The second line cannot be obtained from the first!')
            break
    count_shift += 1
else:
    print('The second line cannot be obtained from the first!')

# зачет!
