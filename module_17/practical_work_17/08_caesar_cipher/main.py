def encrypt_char(key, sym):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    symbol = ' .,:;'
    if symbol.count(sym):
        return sym
    elif alphabet.index(sym) + key > len(alphabet) - 1:
        return alphabet[alphabet.index(sym) + key - (len(alphabet))]
    else:
        return alphabet[alphabet.index(sym) + key]


user_str = input('Enter the phrase in Russian: ')
key = int(input('Enter the shift: '))

encrypt_list = ''.join([encrypt_char(key, symbol) for symbol in user_str])

print(encrypt_list)

# зачет!
