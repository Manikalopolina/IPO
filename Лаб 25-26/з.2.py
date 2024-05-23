import numpy as np

A = np.arange(12, 24)
print("Одномерный массив A:")
print(A)

matrix_3x4 = A.reshape(3, 4)
matrix_4x3 = A.reshape(4, 3)
matrix_2x6 = A.reshape(2, 6)



print("Матрица 3x4:")
print(matrix_3x4)
print("Матрица 4x3:")
print(matrix_4x3)
print("Матрица 2x6:")
print(matrix_2x6)