len_list = int(input('Enter the length of the list: '))
work_list = [1 if i_num % 2 == 0 else i_num % 5 for i_num in range(len_list)]
print(f'Result: {work_list}')

# зачет!
