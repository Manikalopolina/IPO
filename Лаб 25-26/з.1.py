import numpy as np # Импорт библиотеки NumPy


def calculate_determinant(matrix): # Объявление функции calculate_determinant для вычисления определителя матрицы
    determinant=np.linalg.det(matrix)
    return determinant


def solve_linear_equation(matrix_A, vector_b): # Объявление функции solve_linear_equation для решения системы линейных уравнений
    solution=np.linalg.solve(matrix_A, vector_b)
    return solution

# Задание матрицы A и вектора b
matrix_A=np.array([[2, 1], [1, 1]])
vector_b=np.array([3, 2])


determinant=calculate_determinant(matrix_A) # Вычисление определителя матрицы A вызовом функции calculate_determinant
print("Определитель матрицы A:")
print(determinant)


solution=solve_linear_equation(matrix_A, vector_b) # Решение системы уравнений с матрицей A и вектором b
# вызовом функции solve_linear_equation
print("Решение системы уравнений:")
print(solution)
