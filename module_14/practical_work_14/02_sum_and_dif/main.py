def summ_digit(num):
    var_amount = 0
    while num != 0:
        digit = num % 10
        var_amount += digit
        num //= 10
    return var_amount


def count_digits(num):
    count_var = 0
    while num != 0:
        count_var += 1
        num //= 10
    return count_var


while True:
    number = int(input('Enter a number: '))
    if number > 0:
        break
    else:
        print('The number must be an integer and positive!')

summ = summ_digit(number)
count = count_digits(number)
print(f'\nThe sum of the numbers: {summ}')
print(f'The number of the digits in the number: {count}')
print(f'The difference between the sum and the number of digits: {summ - count}')

# зачет!
