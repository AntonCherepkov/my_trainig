class CountIterator:
    def __init__(self):
        self.__counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        number = self.__counter
        self.__counter += 1
        return number


my_iter = CountIterator()
for i_elem in my_iter:
    print(i_elem)
        