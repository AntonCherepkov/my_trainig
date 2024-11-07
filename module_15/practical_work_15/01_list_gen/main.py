number = int(input('Enter the number: '))
list_odd_num = []

# The 1st solution method
for i_num in range(1, number + 1, 2):
    list_odd_num.append(i_num)

# The 2nd solution method
# for i_num in range(1, number // 2 + number % 2 + 1):
#     list_odd_num.append(2 * i_num - 1)

print(f'A list of odd numbers up to {number}: {list_odd_num}')

# зачет!
