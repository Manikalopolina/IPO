import numpy as np # Импорт библиотеки numpy

def swap_halves_array(arr):
    length=len(arr)  # Вычисление длины массива arr
    middle=length//2  # Вычисление середины массива
    first_half, second_half= np.split(arr, [middle]) # разделение массива на две половины
    swapped_array=np.concatenate((second_half, first_half)) # объединение половин в обратном порядке
    return swapped_array  # Возвращение результата

array=np.array([1, 2, 3, 4, 5, 6])  # Создание массива array
result=swap_halves_array(array)
print(result)