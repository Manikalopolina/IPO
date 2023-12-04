class Patient: # Создание класса Patient
    # Определение метода init для инициализации объекта класса
    def __init__(self, name, age, diagnosis, attendingdoctor):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.attendingdoctor = attendingdoctor

    # Определение декораторов для работы с свойствами объекта name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Определение декораторов для работы с свойствами объекта age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    # Определение декораторов для работы с свойствами объекта diagnosis
    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._diagnosis = value

    # Определение декораторов для работы с свойствами объекта attendingdoctor
    @property
    def attendingdoctor(self):
        return self._attendingdoctor

    @attendingdoctor.setter
    def attendingdoctor(self, value):
        self._attendingdoctor = value

    def info(self):# Определение метода info для возвращения информации о пациенте
        return f"Name: {self.name}, Age: {self.age}, Diagnosis: {self.diagnosis}, Attending Doctor: {self.attendingdoctor}"


# Создание экземпляра класса Patient с именем 'Polina', возрастом 86, диагнозом 'angina' и лечащим врачом 'Belush D.R.'
patient = Patient('Polina', 86, 'angina', 'Belush D.R.')
patient.name = 'Fedya' # Установка нового имени 'Fedya'
patient.age = 45 # Установка нового возраста 45
patient.diagnosis = 'bronchitis' # Установка нового диагноза 'bronchitis'
patient.attendingdoctor = 'Manikalo P.A.' # Установка нового лечащего врача 'Manikalo P.A.'
print(patient.info())  # Вывод информации о пациенте (имя, возраст, диагноз, лечащий врач)

