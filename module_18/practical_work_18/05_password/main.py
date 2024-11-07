while True:
    is_check_len = False
    is_check_digit = False
    is_check_title = False
    count_digit = 0

    user_password = input('Come up whith a password: ')
    if user_password.isascii():
        if len(user_password) >= 8:
            is_check_len = True

        for num in range(65, 91):
            if chr(num) in user_password:
                is_check_title = True
                break

        for symbol in user_password:
            if symbol in '0123456789':
                count_digit += 1
                if count_digit == 3:
                    is_check_digit = True
                    break

        if is_check_digit and is_check_len and is_check_title:
            print('The password is relible!')
            break
        else:
            print('The passwoed is unrelible!')
    else:
        print('The password must contain only Latin characters!')

# зачет!
