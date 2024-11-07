def count_letters(text):
    low = sum(1 for letter in text if letter.islower())
    upp = sum(1 for letter in text if letter.isupper())
    return upp, low


user_str = input('Enter the text: ')

uppercase, lowercase = count_letters(user_str)

print(f'Number of uppercase letter: {uppercase}')
print(f'Number of lowercase letter: {lowercase}')

# зачет!
