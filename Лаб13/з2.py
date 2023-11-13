
class Rub(object):
    '''Класс для работы с рублями и копейками.'''
    def __init__(self, rub=0, kop=0): # Определение метода инициализации объекта класса Rub
        self.rub=rub # Инициализация атрибута rub объекта класса Rub
        self.kop=kop # Инициализация атрибута kop объекта класса Rub
        self.normalize() # Вызов метода normalize для нормализации значений rub и kop

    def normalize(self): # Определение метода normalize, который нормализует значения rub и kop
        self.rub+=self.kop//100 # Добавление целой части от деления kop на 100 к rub
        self.kop=self.kop % # Оставление остатка от деления kop на 100 в kop

    def __str__(self): # Определение метода преобразования объекта в строку
        return f"{self.rub}.{self.kop:02d} rub"  # Возвращение строки в формате "rub.kop rub"

    def __lt__(self, other): # Определение метода сравнения меньше для объектов класса Rub
        if self.rub<other.rub: # Если rub объекта self меньше rub объекта other
            return True # Возвращение True
        elif self.rub==other.rub and self.kop<other.kop:  # Если rub объекта self равен rub объекта other и kop объекта
            # self меньше kop объекта other
            return True # Возвращение True
        return False # Возвращение False

    def __add__(self, other): # Определение метода сложения для объектов класса Rub
        res=Rub(self.rub + other.rub, self.kop + other.kop) # Создание нового объекта Rub с суммой rub и kop объектов self и other
        res.normalize() # Вызов метода normalize для нормализации значений rub и kop нового объекта res
        return res # Возвращение нового объекта Rub


class Goods(object):
    ''' Класс описания товара: название и цена '''
    def __init__(self, name='', price=0):  # Определение метода инициализации объекта класса Goods
        self.name=name # Инициализация атрибута name объекта класса Goods
        self.price=price # Инициализация атрибута price объекта класса Goods

# Входные данные
input_data = [
    "rice 10.50",
    "tea 6.30",
    "cake 10.12",
    "salad 20.00"]

# Обработка входных данных
goods=[] # Создание пустого списка для хранения объектов класса Goods
total_price=Rub() # Создание объекта Rub для хранения общей суммы цен товаров

for line in input_data: # Перебор строк во входных данных
    name, price_str = line.split() # Разделение строки на название и цену товара
    rub, kop = map(int, price_str.split('.')) # Разделение строки на название и цену товара
    price = Rub(rub, kop) # Создание объекта Rub с заданными значениями rub и kop
    goods.append(Goods(name, price))# Добавление объекта Goods с заданным названием и ценой в список товаров
    total_price += price # Добавление цены товара к общей сумме


goods.sort(key=lambda x: x.price, reverse=True)# Сортировка списка товаров по убыванию цены


for good in goods:# Сортировка списка товаров по убыванию цены
    print(good.name, good.price)# Вывод названия и цены товара

print('-----')
print(f"total {total_price} rub")# Вывод общей суммы цен товаров


