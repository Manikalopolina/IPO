import numpy as np # Импорт библиотеки NumPy

A=np.arange(13) # Создание одномерного массива A
print("Одномерный массив A:")
print(A)

C=A.reshape(4, 3) # Преобразование одномерного массива A в двумерную матрицу размером 4x3
print("Матрица C (4x3):")
print(C)

CT=C.T # Получение транспонированной матрицы CT путем транспонирования матрицы C
print("Транспонированная матрица CT (3x4):")
print(CT)

B=np.dot(C, CT) # Умножение матрицы C на транспонированную матрицу CT для получения матрицы B
print("Матрица B (результат умножения C на CT):")
print(B)