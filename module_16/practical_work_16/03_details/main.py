shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail_search = input('Enter the detail: ')
count_detail = 0
sum_price = 0

for detail, cost in shop:
    if detail == detail_search:
        count_detail += 1
        sum_price += cost
else:
    if count_detail == 0:
        print('This part is not available')

print(f'Number of {detail_search} in stock: {count_detail}')
print(f'Total cost of parts: {sum_price}')

# зачет!
