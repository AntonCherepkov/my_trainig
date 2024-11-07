# Это второй способ решения задачи. Сложность алгоритма здесь составляет примерно О(n/2), т.к. за один проход цикла мы
# обрабатываем два элемента (формируем подстроки) из двух строк. Таким образом мы смогли упростить алгоритм в корень из
# двух раз

str_1 = 'qwertyU'
str_2 = 'rtyUqwe'
count_shift = 0

for i in range(0, len(str_1)+1):
    buf_1 = str_1[:(-i if i != 0 else len(str_1))]
    buf_2 = str_2[i:len(str_2)]
#    print(buf_1, '\t|', buf_2)
    if buf_1 == buf_2:
        buf_1 = str_1[len(str_1)-i:len(str_1)]
        buf_2 = str_2[:i]
#        print(buf_1, '\t|', buf_2)
        if buf_1 == buf_2:
            print(f"The second line is obtained from the first with a shift of {count_shift}")
            break
        else:
            print('The second line cannot be obtained from the first!')
            break
    count_shift += 1
else:
    print('The second line cannot be obtained from the first!')