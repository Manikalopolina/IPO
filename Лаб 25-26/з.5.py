import numpy as np   # Импорт библиотеки NumPy

def createarray():  # Объявление функции createarray, которая создает массив А размером 5x2 с заданными значениями
    A=np.array([[1, 6], [2, 8], [3, 11], [3, 10], [1, 7]])
    return A

A=createarray()  # Создание массива A вызовом функции createarray()
AT=np.transpose(A)  # Транспонирование матрицы A с помощью функции transpose из библиотеки NumPy
print("Матрица А:")
print(A)
print("Матрица АТ:")
print(AT)
