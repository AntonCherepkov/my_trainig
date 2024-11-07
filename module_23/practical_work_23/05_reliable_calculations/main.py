def get_sage_sqrt(num):
    try:
        if not isinstance(num, (int, float)):
            raise TypeError('Значение должно быть числом!')
        if num <= 0:
            raise ValueError('Значение должно быть больше нуля!')

        return num ** 0.5
    # TODO тут кстати можно отлавливать 1 раз все ошибки и логгировать, в данном случае можно объеждинить
    except (TypeError, ValueError, Exception) as e_error:
        return f'Error: {e_error}'



# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")

# зачет!
