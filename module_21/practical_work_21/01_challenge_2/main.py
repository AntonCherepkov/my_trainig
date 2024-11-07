def show_number(number):
    if number == 0:
        return None

    show_number(number - 1)
    print(number)


user_number = int(input('Введите число: '))

show_number(user_number)

# зачет!
