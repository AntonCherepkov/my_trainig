a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
five_elem = a.count(5)
print(f'The number of digits is 5: {five_elem}')
for _ in range(five_elem):
    a.remove(5)
a.extend(c)

print(f'The number of digits is 3: {a.count(3)}')
print(f'The final list: {a}')

# зачет!
