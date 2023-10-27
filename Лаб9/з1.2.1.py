import з2

x = (1, 2, 3)
y = (4, 5, 6)
z = (7, 8, 9)
t = (10, 11, 12)

min_distance, closest_points =з2.find_min_distance(x, y, z, t)

print("Минимальное расстояние:", min_distance)
print("Точки, находящиеся на минимальном расстоянии друг от друга:", closest_points)
