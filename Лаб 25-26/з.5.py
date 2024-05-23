import numpy as np


def createarray():
    A = np.array([[1, 6], [2, 8], [3, 11], [3, 10], [1, 7]])
    return A


A = createarray()
AT = np.transpose(A)
print("Матрица А:")
print(A)
print("Матрица АТ:")
print(AT)
