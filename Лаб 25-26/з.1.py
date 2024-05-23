import numpy as np


def cal_determinant(matrix):
    determinant=np.linalg.det(matrix)
    return determinant


def solve_linear_equation(matrix_A, vector_b):
    solution=np.linalg.solve(matrix_A, vector_b)
    return solution


matrix_A = np.array([[4, 1], [5, 1]])
vector_b = np.array([2, 5])


determinant = cal_determinant(matrix_A)
print("Определитель матрицы A:")
print(determinant)


solution = solve_linear_equation(matrix_A, vector_b)
print("Решение системы уравнений:")
print(solution)
