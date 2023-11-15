class ChemicalElement:
    '''Класс, описывающий сведения о химическом элементе.'''

    def __init__(self, name, symbol, atomic_number, atomic_mass, boiling_point, melting_point):
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.atomic_mass = atomic_mass
        self.boiling_point = boiling_point
        self.melting_point = melting_point

    def set_name(self, name):
        self.name = name

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_atomic_number(self, atomic_number):
        self.atomic_number = atomic_number

    def set_atomic_mass(self, atomic_mass):
        self.atomic_mass = atomic_mass

    def set_boiling_point(self, boiling_point):
        self.boiling_point = boiling_point

    def set_melting_point(self, melting_point):
        self.melting_point = melting_point

    def chemical_element_info(self):
        info = f'Название: {self.name}\nСимвол элемента: {self.symbol}\nАтомный номер: {self.atomic_number}\nАтомная масса: {self.atomic_mass}\nТемпература кипения: {self.boiling_point}\nТемпература плавления: {self.melting_point}\n'
        return info

    def get_name(self):
        '''Метод для получения названия элемента.'''
        return self.name

    def get_symbol(self):
        '''Метод для получения символа элемента.'''
        return self.symbol

    def get_atomic_number(self):
        '''Метод для получения атомного номера элемента.'''
        return self.atomic_number


# Создание и инициализация экземпляров класса
elements = []
for i in range(5):
    name = input("Введите название элемента: ")
    symbol = input("Введите символ элемента: ")
    atomic_number = int(input("Введите атомный номер элемента: "))
    atomic_mass = float(input("Введите атомную массу элемента: "))
    boiling_point = int(input("Введите температуру кипения: "))
    melting_point = int(input("Введите температуру плавления: "))
    element = ChemicalElement(name, symbol, atomic_number, atomic_mass, boiling_point, melting_point)
    elements.append(element)

# Вывод информации об элементах
for element in elements:
    print(element.chemical_element_info())
