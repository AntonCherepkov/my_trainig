user_str = input('Enter the string: ').split()

# Первый способ не переводит в верхний регистр символ после апострофа
result_str = ' '.join([word.capitalize() for word in user_str])

# Второй способ проще, но к сожалению переводит в верхний регистр символ после апострофа
result_str_2 = ' '.join(user_str).title()

print(result_str)
print(result_str_2)

# зачет!
