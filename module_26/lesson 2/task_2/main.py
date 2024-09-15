from random import random


class RandomNumbers:
    def __init__(self, size_list):
        self.__count = 0
        self.result_val = 0
        self.size_list = size_list

    def __iter__(self):
        self.start_val = 0
        self.stop_val = 1
        self.__count = 0
        return self

    def __next__(self):
        self.__count += 1
        if self.__count > self.size_list:
            raise StopIteration('Достигнут предел итераций!')
        self.result_val = round((self.result_val + random()), 2)
        return self.result_val

list_num = RandomNumbers(5)
for i_elem in list_num:
    print(i_elem)

print()

list_num = RandomNumbers(6)
for i_elem in list_num:
    print(i_elem)
    