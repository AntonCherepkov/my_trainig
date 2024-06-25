import os


def count_letters(word):
    return {
        letter: sum(1 for i_letter in word if i_letter == letter)
        for letter in word
    }


def is_palindrome(in_word):
    count_dict = count_letters(in_word)
    numb_even_grouper = 0
    numb_odd_grouper = 0
    for letter, counter in count_dict.items():
        if counter % 2 == 0:
            numb_even_grouper += 1
        else:
            numb_odd_grouper += 1
    if numb_odd_grouper > 1:
        return False
    else:
        return True


path_file = os.path.abspath(os.path.join('words.txt'))
path_errors_log = os.path.abspath(os.path.join('errors.log'))
with open(path_file, 'r', encoding='utf-8') as in_file:
    for word in in_file:
        try:
            if word.endswith('\n'):
                word = word.rstrip('\n')
            if not word.isalpha():
                raise TypeError
        except TypeError as exc:
            with open(path_errors_log, 'a', encoding='utf-8') as errors_file:
                errors_file.write(
                    'Найдено число в слове '
                    + word
                    + '\n'
                )
