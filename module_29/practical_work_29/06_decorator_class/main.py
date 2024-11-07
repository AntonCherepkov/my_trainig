from loggerdecorator import LoggerDecorator


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется сложный алгоритм
    result = 0
    with open('test.txt', 'a+', encoding='utf8') as file:
        for i in range(arg1):
            for j in range(arg2):
                file.write(str(i + j) + ' ')
                result += i + j
            file.write('\n')
        file.write(f'Итоговое число: {result}')
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)