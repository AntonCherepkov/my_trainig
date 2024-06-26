print('Задача из внеурочного занятия 1.')
# Требуется определить индекы первого и последнего вхождения буквы в строке. Для этого нужно написать функцию 
# first_last(letter, str), включающую два параметра: letter - искомый символ, str - целевая строка. В случае отсутствия 
# буквы в строке, нужно вернуть кортеж (None, None), если же она есть, то кортеж будет состоять из первого и последнего 
# индекса этого символа.


# Здесь можно применить также и метод .find(), в этом случае не возникнет ошибки, если в целевой строке не окажется искомой 
# подстроки. Однако в моём случае её и так не окажется, ведь перед применением метода .index()
 
def first_last(letter, str):
    if str.count(letter) >= 1:
        return (user_str.index(letter),
                user_str.rindex(letter))
    return (None, None)


user_str = "I'm Anton! I'm from Russia"
search_str = 'm'

beg_index, end_index = first_last(search_str, user_str)

print('The index of the first occurrence of the charter "{0}": {1}, and the last: {2}'.format(
    user_str,
    beg_index,
    end_index
))