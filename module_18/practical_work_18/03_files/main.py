file_name = input('Enter the file name: ')
forbidden_char = ['@', '№', '$', '^', '&', '*', '(', ')']

for symbol in forbidden_char:
    if file_name.startswith(symbol):
        print('Error: the name starts with an invalid character')
        break
else:
    for extension in ['.txt', '.docx']:
        if file_name.endswith(extension):
            print('The file name is correct!')
            break
    else:
        print('You need to choose another extension')

# зачет!
