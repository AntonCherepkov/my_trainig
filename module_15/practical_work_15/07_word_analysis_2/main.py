import math
word_user = list(input('Enter the word: '))
is_palindrome = True

i_left = math.floor(len(word_user) / 2) - 1
i_right = math.ceil(len(word_user) / 2)
while i_right <= len(word_user) and i_left >= 0:
    if word_user[i_left] != word_user[i_right]:
        is_palindrome = False
        break
    i_left -= 1
    i_right += 1

if is_palindrome:
    print('The word is a palindrom')
else:
    print('The word is not a palindrom')

# зачет!
