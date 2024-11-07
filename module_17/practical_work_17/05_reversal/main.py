while True:
    user_str = input('Enter of the string: ')
    if user_str.count('h') < 2:
        print('The string must contain at least two "h" characters')
    else:
        break

# list comprehension
revers_list = ''.join([user_str[i_sym] for i_sym in range(len(user_str) - 1)
                      if user_str.index('h') < i_sym < user_str.rindex('h')][::-1])

print(revers_list)

# срез строки
revers_str = user_str[user_str.rindex('h') - 1:user_str.index('h'):-1]

print(revers_str)

# зачет!
