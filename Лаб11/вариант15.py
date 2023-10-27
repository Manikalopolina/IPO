class ChemicalElement:
    '''Класс, описывающий сведения о химическом элементе.'''
    def __init__(self, name, symbol, atomic_number, atomic_mass, boiling_point, melting_point):
        self.name = name  # название элемента
        self.symbol = symbol  # символ элемента
        self.atomic_number = atomic_number  # атомный номер
        self.atomic_mass = atomic_mass  # атомная масса
        self.boiling_point = boiling_point  # температура кипения
        self.melting_point = melting_point  # температура плавления

    def chemicalelement_info(self):
        info = f'Название: {self.name}\nСимвол Элемента: {self.symbol}\nАтомный Номер: {self.atomic_number} \nАтомная Масса: {self.atomic_mass} \nТемпература Кипения: {self.boiling_point}\nТемпература Плавления: {self.melting_point}'
        return info
    def get_name(self):
        ''' Метод для получения названия элемента.'''
        return self.name
    def get_symbol(self):
        ''' Метод для получения символа элемента.'''
        return self.symbol
    def get_atomic_number(self):
        ''' Метод для получения атомного номера элемента.'''
        return self.atomic_number
    def get_atomic_mass(self):
        ''' Метод для получения атомной массы элемента.'''
        return self.atomic_mass

# Создание и инициализация экземпляров класса
element1 = ChemicalElement("Кислород", "O", 8, 15.999, -183, -218)
element2 = ChemicalElement("Углерод", "C", 6, 12.011, 3550, 3550)
element3 = ChemicalElement("Железо", "Fe", 26, 55.845, 2750, 1538)
element4 = ChemicalElement("Азот", "N", 7, 14.007, -196, -210)
element5 = ChemicalElement("Натрий", "Na", 11, 22.990, 883, 97)
print(element1.chemicalelement_info())
print(element2.chemicalelement_info())
print(element3.chemicalelement_info())
print(element4.chemicalelement_info())
print(element5.chemicalelement_info())

