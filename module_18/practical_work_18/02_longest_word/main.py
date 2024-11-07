user_str = input('Введите строку: ').split()

len_words = [len(word) for word in user_str]
index_max_word = len_words.index(max(len_words))

if max(len_words) % 10 == 1:
    word_ending = ''
elif max(len_words) % 100 in range(10, 21):
    word_ending = 'ов'
elif max(len_words) % 10 in [0, 2, 3, 4]:
    word_ending = 'а'
elif max(len_words) % 10 in range(5, 10):
    word_ending = 'ов'

print('Самое длинное слово: ', user_str[index_max_word])
print('Длина этого слова: {:d} символ{:s}'.format(
    max(len_words),
    word_ending
))

# зачет!
