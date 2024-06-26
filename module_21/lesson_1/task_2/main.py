print('Задача 2. Степень числа')
# На одном из форумов, посвященному программированию, пользователь выложил такой код для расчета степени числа
# без использования циклов, ** и функции math.pow():
# 
# def power(a, n):
#   return a * power(a, n)
# 
# float_num = float(input('Введите вещественное число: '))
# int_num = int(input('Введите степень числа: '))
# 
# prin(float_num, '**', int_num, '=', power(float_num, int_num))
# 
# Другие пользователи отметили, что это решение не рабочее и в нем есть ошибки. Исправте решение, не используя 
# циклы, возведение в степень через оператор ** и функцию math.pow()

def power(num, degree):
    if degree <= 1:
        return num
    result = power(num, degree - 1)     # Это рекурсия, передаем переменной result значение произведения из 
    return result * num                 # предыдущего вызова


float_num = float(input('Введите вещественное число: '))
int_num = int(input('Введите степень числа: '))

result = power(float_num, int_num)

print(f'{float_num} ** {int_num} = {result}')
