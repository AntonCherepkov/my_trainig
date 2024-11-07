from random import randint

start_list =  [
    randint(0, 9) for _ in range(10)
]

print(f'Начальный список: {start_list}')

# Первый способ банальный - идти циклом по стартовому списку, и отщипывая по два элемента, присоединять в виде
# кортежа к итоговому списку

result_var_1 = list()
for i_num in range(1,(len(start_list)) + 1, 2):
    double_num = tuple()
    double_num = start_list[i_num-1], start_list[i_num]
    result_var_1.append(double_num)

print(f'Первый вывод: {result_var_1}')

# Второй способ трудоёмкий - генерируя два списка из стартового с четными и нечетными элементами, склеивать их
# с помощью zip() и в конечном итоге передать итоговому списку

result_var_2 = list(zip([start_list[i_num] for i_num in range(0, len(start_list), 1) if i_num % 2 == 0],
                        [start_list[i_num] for i_num in range(0, len(start_list), 1) if i_num % 2 != 0]
))

print(f'Второй вывод: {result_var_2}')

# зачет!
