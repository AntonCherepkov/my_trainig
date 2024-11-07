import math
def smallest_divisor(num):
    for num_i in range(2, num + 1, 1):
        if num % num_i == 0:
            return num_i


while True:
    number = int(input('Enter a number: '))
    if number <= 1:
        print('Enter a natural number greeter then one!')
    else:
        break

print(smallest_divisor(number))

# зачет!
