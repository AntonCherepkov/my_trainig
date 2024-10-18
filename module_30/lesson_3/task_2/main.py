result = list(filter(
                lambda x: not x.isdigit() and not x.istitle(),
                list(input('Enter the string: '))
                ))

print(result)