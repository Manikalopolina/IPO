import numpy as np

A = np.arange(12)
print("Одномерный массив A:")
print(A)

C = A.reshape(4, 3)
print("Матрица C (4x3):")
print(C)

CT = C.T
print("Транспонированная матрица CT (3x4):")
print(CT)

B = np.dot(C, CT)
print("Матрица B (результат умножения C на CT):")
print(B)