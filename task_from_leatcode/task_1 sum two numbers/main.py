class MatrixClass:
    def __init__(self, matrix, number):
        self.matrix = matrix
        self.number = number

    def search_indexes(self):
        for i in range(0, len(self.matrix) - 1, 1):
            for j in range(i + 1, len(self.matrix), 1):
                if self.matrix[i] + self.matrix[j] == self.number:
                    return [i, j]
        else:
            print('Сумма каждого числа с каждым числом матрицы не даст желаемого результата!')

test_1 = [1, 2, 3, 4, 5, 6]
my_matrix = MatrixClass(test_1, 9)
print(my_matrix.search_indexes())
