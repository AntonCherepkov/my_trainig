print('Шифр цезаря 2')
# Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря. Напомним, что в таком способе шифрования каждая 
# буква заменяется на следующую по алфавиту через К позиций по кругу.
# Напишите программу, которая реализует этот алгоритм шифрования. Не используйте конкатенацию и сделайте так, что бы текст 
# был в одном регистре.

begin_text = (input('Enter the text in Russian: ')).lower()
shift = int(input('Enter the number of shift: '))
alphabet = [chr(symbol) for symbol in range(ord('a'), ord('я') + 1)]

encr_text = ''.join([alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
                    if letter in alphabet else letter
                    for letter in begin_text.lower()
])

print(encr_text)