print('Задача 1. Улучшенная лингвистика')
# Усовершенствуйте старую программу:
# У нас есть список из трёх слов, которые вводит пользователь. Затем вводится сам текст произведения, который вводится 
# уже в одну строку. Напишите программу, которая посчитает, сколько раз слова пользователя встречаются в тексте.

user_word = input('Enter the shearch words sepereted by a space: ').split()
text = input('Enter the text: ')

result_analysis = [[word, text.count(word)] for word in user_word]

template_output = 'В тексте встречается {0} раз слово {1}'
for word, count in result_analysis:
    print(template_output.format(
        count,
        word))
