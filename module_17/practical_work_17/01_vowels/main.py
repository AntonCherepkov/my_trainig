def check_vowel_letters(symbol):
    vowel_let = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    for vowel in vowel_let:
        if symbol == vowel or symbol.lower() == vowel:
            return True


user_text = input('Enter the text: ')

result_list_2 = [sym for sym in user_text if check_vowel_letters(sym)]

print(result_list_2)

# зачет!
