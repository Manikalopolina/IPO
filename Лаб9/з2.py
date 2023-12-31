import math

def distance(x, y):
    '''
    Функция вычисляет расстояние между двумя точками в трехмерном пространстве.
    Аргументы:
    x (tuple): Координаты первой точки в формате (x1, x2, x3).
    y (tuple): Координаты второй точки в формате (y1, y2, y3).
    Возвращаемое значение:
    float: Расстояние между двумя точками.'''
    return math.sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2 + (y[2] - x[2])**2)

def find_min_distance(x, y, z, t):
    '''Функция находит точки,находящиеся на минимальном расстоянии друг от друга, и возвращает это минимальное расстояние
    Аргументы:
    x (tuple): координаты первой точки в формате(x1,x2,x3)
    y (tuple): координаты второй точки в формате(y1,y2,y3)
    z (tuple): координаты третьей точки в формате(z1,z2,z3)
    t (tuple): оординаты четвёртой точки в формате(t1,t2,t3)
    Возвращаемое значение:
    tuple:минимальное расстояние и список точек, находящихся на этом расстоянии
    '''
    distances = [(x, y), (x, z), (x, t), (y, z), (y, t), (z, t)]
    min_distance = float('inf')
    closest_points = []

    for p in distances:
        dist = distance(p[0], p[1])# Вычисление расстояния между 2 точками
        if dist < min_distance:# если текущее расстояние меньше минимального, то минимальное расстояние и список точек обновляется
            min_distance = dist
            closest_points = [p]
        elif dist == min_distance:# если текущее расстояние равно минимальному, то добавляется пара точек в список
            closest_points.append(p)

    return min_distance, closest_points

