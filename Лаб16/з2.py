class Patient:
    def __init__(self, name, age, diagnosis, attendingdoctor):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.attendingdoctor = attendingdoctor

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._diagnosis = value

    @property
    def attendingdoctor(self):
        return self._attendingdoctor

    @attendingdoctor.setter
    def attendingdoctor(self, value):
        self._attendingdoctor = value

    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Diagnosis: {self.diagnosis}, Attending Doctor: {self.attendingdoctor}"



patient = Patient('Polina', 86, 'angina', 'Belush D.R.')
patient.name = 'Fedya'
patient.age = 45
patient.diagnosis = 'bronchitis'
patient.attendingdoctor = 'Manikalo P.A.'
print(patient.info())

