ip_address = input('Enter the IP-address: ')

if len(ip_address.split('.')) == 4:
    for number in ip_address.split('.'):
        if not(number.isdigit()):
            print(f'{number} - is not an integer')
            break
        elif int(number) > 255:
            print(f'{number} should not exceed 255')
            break
    else:
        print('IP-address is correct')
else:
    print('Address is four numbers separated by a dot')

# зачет!
