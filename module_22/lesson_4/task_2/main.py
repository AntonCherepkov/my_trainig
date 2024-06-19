import os


def count_letters(word):
    return {
        letter: sum(1 for i_letter in word if i_letter == letter)
        for letter in word
    }


def is_palindrome(count_dict):
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


for word in 'asdddsa', 'adddaaghkkll':
    count_let = count_letters(word)
    print(is_palindrome(count_let))



