import numpy as np # Импорт библиотеки NumPy
# Определение среднего значения и стандартного отклонения для нормального распределения
mean=0
std_dev=1.0
array_3x4=np.random.normal(mean, std_dev, (3, 4)) # Генерация двумерного массива размером 3x4 из нормального
# распределения
print("Массив 3x4 из нормального распределения:")
print(array_3x4)

array_1d=array_3x4.flatten() # Преобразование двумерного массива array_3x4 в одномерный массив
# с сохранением порядка элементов
print("Одномерный массив с таким же size:")
print(array_1d)