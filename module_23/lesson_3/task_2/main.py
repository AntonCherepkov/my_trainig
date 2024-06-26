import os, math

def search_palindrom(*words, sym_lst=None):
    if sym_lst is None:
        sym_lst = []

    left, rigth = '', ''
    for word in words:
        print(word)
        if len(word) % 2 != 0:
            left = word[:int(len(word) / 2)]
            rigth = word[int(len(word) / 2) + 1:][::-1]
        
        
        print('left: ', left)
        print('right: ', rigth)
        # elif len(word) % 2 == 0:
        #     left = word[]


print(search_palindrom('ufafu', 'adsasda', 'lkjhghjkl'))
