def char_count(work_str):
    result_list = []
    while work_str != '':
        elem = [work_str[0], str(len(work_str) - len(work_str.lstrip(work_str[0])))]
        result_list.append(elem)
        work_str = work_str.lstrip(work_str[0])
    return result_list


user_str = input('Enter the string: ')

encrypt_str = ''.join([result_str for elem in char_count(user_str)
                                  for result_str in elem])

print(f'Encrypted string: {encrypt_str}')

# зачет!
