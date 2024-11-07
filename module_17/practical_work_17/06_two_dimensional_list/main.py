def create_list(num, row, col):
    nested_list = [number for number in range(num, row * col - (row - num) + 1, row)]
    return nested_list


row = int(input('Enter the number of the string: '))
col = int(input('Enter the number of the row: '))

result_list = [create_list(num, row, col) for num in range(1, row + 1)]

print(result_list)

# зачет!
