import numpy as np
mean = 0 # среднее отклонение
std_dev = 1.0 # среднеквадратичное отклонение
array_ = np.random.normal(mean, std_dev, (3, 4))
print("Массив 3x4 из нормального распределения:")
print(array_)
array_1d = array_.flatten()
print("Одномерный массив с таким же атрибутом size:")
print(array_1d)