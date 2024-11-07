from matrix_method import MatrixClass


test_1 = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9], 
    [10, 11, 12]
]

test_2 = [
    [4, 5, 6, 7],
    [7, 8, 9, 8],
    [10, 11, 12, 9]
]
    
matrix_1 = MatrixClass(test_1)
matrix_2 = MatrixClass(test_2)

matrix_3 = matrix_1 * matrix_2

matrix_1.show_matrix()
print('* ', '-' * 20)
matrix_2.show_matrix()
print('= ', '-' * 20)
matrix_3.show_matrix()
print(matrix_3.matrix)

print('\nTransposition ZIP():')
matrix_3.transposition_zip()
matrix_3.show_matrix()

print('\nTransposition List Comprehensions:')
matrix_3.transposition_lc()
matrix_3.show_matrix()

# зачет!
