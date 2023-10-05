artists = {"Leonardo da Vinci": 1452,"Pablo Picasso": 1881, "Vincent van Gogh": 1853,"Michelangelo": 1475, "Rembrandt": 1606,
           "Claude Monet": 1840,"Salvador Dali": 1904}# Создаём словарь с именами художников и их годы рождения
while True:
     for artist, birth_year in artists.items():# Перебор всех пар ключ-значение в словаре
        print(artist, ":", birth_year)# Выводим каждого художника и его год рождения
     key = input("Введите ключ:(Введите 'стоп' для остановки запроса) ")# Запрашиваем у пользователя ключ
     if key=='стоп':# Проверка на значенте 'стоп'  для выхода из цикла
        break
     value = artists.get(key)# Поиск значения по введённому ключу
     # Проверяем, есть ли значение для данного ключа в словаре и выводим его
     if value:
        print("Значение:", value)
     else:
        print("Ключ не найден")



