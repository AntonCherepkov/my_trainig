info_count = {
    1: 'Первая пара',
    2: 'Вторая пара',
    3: 'Третья пара',
    4: 'Четвертая пара',
    5: 'Пятая пара',
    6: 'Шестая пара',
    7: 'Седьмая пара',
    8: 'Восьмая пара',
    9: 'Девятая пара',
    10: 'Десятая пара'
}

synonyms_dict = dict()
num_pairs = int(input('Введите количество пар: '))

print('\nВведите синонимы через дифис:')
for num_pair in range(1, num_pairs + 1, 1):
    print(f'{info_count[num_pair]}:', end=' ')
    synonyms = input().lower()
    synonyms_dict[info_count[num_pair]] = synonyms.split(' - ')
print()

is_exit = False
while True:
    user_word = input('Введите слово: ').lower()
    for words in synonyms_dict.values():
        if user_word in words:
            synonym_words = words[:]
            synonym_words.remove(user_word)
            print(f'Синоним слову {user_word} - {synonym_words[0]}')
            is_exit = True
    if is_exit:
        break
    else:
        print('Нет такого слова')

# зачет!
