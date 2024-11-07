from my_error import MatixDimensionError

class MatrixClass:
    def __init__(self, matrix):
        try:
            self.matrix = matrix
            self.row, self.col = self.determine_dimension(matrix)
            if self.col is None:
                raise MatixDimensionError('Попытка инициализации не квадратной матрицей!')
        
        except MatixDimensionError as mde:
            print('Error: ', mde)

    def show_matrix(self):
        for row in self.matrix:
            for col in row:
                print(col, end=' ')
            print()

    def determine_dimension(self, in_array):        
        row = sum(1 for row in in_array)
        all_col = [sum(1 for col in i_row) for i_row in in_array]

        for i_col in range(len(all_col) - 1):
            if all_col[i_col] != all_col[i_col + 1]:
                return None, None
        else:
            return row, all_col[1]

    def is_equality_check(self, second_matrix):
        if isinstance(second_matrix, MatrixClass):
            if self.row == second_matrix.row and self.col == second_matrix.col:
                return True
            return False
        
    def is_check_possibility_mult(self, second_matrix):
        if isinstance(second_matrix, MatrixClass):
            if self.row == second_matrix.col and self.col == second_matrix.row:
                return True
            return False     
        
    def __add__(self, second_matrix):
        if self.is_equality_check(second_matrix):
            result = MatrixClass(
                [
                    [
                        self.matrix[i_row][i_col] + second_matrix.matrix[i_row][i_col]
                        for i_col in range(len(self.matrix[i_row]))
                    ]
                    for i_row in range(len(self.matrix))
                ]
            )
            return result
        else:
            return None

    def __sub__(self, second_matrix):
        if self.is_equality_check(second_matrix):
            result = MatrixClass(
                [
                    [
                        self.matrix[i_row][i_col] - second_matrix.matrix[i_row][i_col]
                        for i_col in range(len(self.matrix[i_row]))
                    ]
                    for i_row in range(len(self.matrix))
                ]
            )
            return result
        else:
            return None

    def __mul__(self, second_matrix):
        if self.is_check_possibility_mult(second_matrix):
            result_lst = [[0] * len(second_matrix.matrix[0]) for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(second_matrix.matrix[0])):
                    for k in range(len(second_matrix.matrix)):
                        result_lst[i][j] += self.matrix[i][k] * second_matrix.matrix[k][j]
            return MatrixClass(result_lst)
        else:
            return None

    def transposition_zip(self):
        self.matrix = [
            list(i) for i in zip(*self.matrix)
        ]

    def transposition_lc(self):
        self.matrix = [
            [self.matrix[j][i] for j in range(len(self.matrix))]
            for i in range(len(self.matrix[0]))
        ]
