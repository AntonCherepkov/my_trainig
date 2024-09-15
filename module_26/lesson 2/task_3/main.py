class PrimeNum:
    def __init__(self, size_list):
        self.cur_num = 2
        self.size_list = size_list

    def __iter__(self):
        return self

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def __next__(self):
        while self.cur_num <= self.size_list:
            if self.is_prime(self.cur_num):
                prime_num = self.cur_num
                self.cur_num += 1
                return prime_num
            self.cur_num += 1
        raise StopIteration


prime_list = PrimeNum(50)
for num in prime_list:
    print(num, end=' ')
