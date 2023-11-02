class ChemicalElement:
    '''Класс, описывающий сведения о химическом элементе.'''
    def __init__(self):
        self._name = None
        self._symbol = None
        self._atomic_number = None
        self._atomic_mass = None
        self._boiling_point = None
        self._melting_point = None

    def set_name(self, name):
        self._name = name

    def set_symbol(self, symbol):
        self._symbol = symbol

    def set_atomic_number(self, atomic_number):
        self._atomic_number = atomic_number

    def set_atomic_mass(self, atomic_mass):
        self._atomic_mass = atomic_mass

    def set_boiling_point(self, boiling_point):
        self._boiling_point = boiling_point

    def set_melting_point(self, melting_point):
        self._melting_point = melting_point

    def chemicalelement_info(self):
        info = f'Название: {self._name}\nСимвол Элемента: {self._symbol}\nАтомный Номер: {self._atomic_number} \nАтомная Масса: {self._atomic_mass} \nТемпература Кипения: {self._boiling_point}\nТемпература Плавления: {self._melting_point}'
        return info

    def get_name(self):
        ''' Метод для получения названия элемента.'''
        return self._name

    def get_symbol(self):
        ''' Метод для получения символа элемента.'''
        return self._symbol

    def get_atomic_number(self):
        ''' Метод для получения атомного номера элемента.'''
        return self._atomic_number

    def get_atomic_mass(self):
        ''' Метод для получения атомной массы элемента.'''
        return self._atomic_mass

# Создание и инициализация экземпляров класса
elements = []
for i in range(5):
    element = ChemicalElement()
    name = input("Введите название элемента: ")
    symbol = input("Введите символ элемента: ")
    atomic_number = int(input("Введите атомный номер элемента: "))
    atomic_mass = float(input("Введите атомную массу элемента: "))
    boiling_point = int(input("Введите температуру кипения: "))
    melting_point = int(input("Введите температуру плавления: "))
    element.set_name(name)
    element.set_symbol(symbol)
    element.set_atomic_number(atomic_number)
    element.set_atomic_mass(atomic_mass)
    element.set_boiling_point(boiling_point)
    element.set_melting_point(melting_point)
    elements.append(element)
# Вывод информации об элементах
for element in elements:
    print(element.chemicalelement_info())
