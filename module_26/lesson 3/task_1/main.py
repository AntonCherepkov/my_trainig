def counter_gen(max_count=999):
    count=0
    while True:
        yield count
        count += 1
        if count > max_count:
            return


def prime_gen(number=50):
    all_num = []
    for num in range(2, number + 1):
        for div in range(2, int(num ** 0.5) + 1):
            if num % div == 0:
                break
        else:
            all_num.append(num)
            yield num


gen_obj = prime_gen()
for num in gen_obj:
    print(num, end=' ')


