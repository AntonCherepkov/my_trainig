print('Задача из внеурочного занятия 2.')
# На основании представленного обрывка текста определить три наиболее часто встречающихся символа в ней. Пробелы нужно 
# игнорировать (не учитывать при подсчёте). Для выделения результатов вычислений требуется написать функцию top3(str). 
# Итог работы функции представить в виде строки: "символ - количество раз, символ - количество раз..."

# Частично сделал задание, осталось лишь 

def top3(user_str):
    num_symbol = [(x, my_str.count(x)) for i, x in enumerate(user_str) 
                   if not x in user_str[:i] and x != ' ']
    
    print(num_symbol)
    
    result_list = []
    for _ in range(3):
        buf_list = [elem for elem in num_symbol 
                    if max(y for x, y in num_symbol) == elem[1]]
        print(buf_list)
        result_list.append(buf_list)
        num_symbol.remove(buf_list[0])
    
    return result_list

my_str = 'aa BBB cccc DDDD x cc CC'
print(top3(my_str))
