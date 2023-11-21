class Stomatology:
    def __init__(self, name, address, city, doctors_count):
        self.name = name
        self.address = address
        self.city = city
        self.doctors_count = doctors_count


class Department(Stomatology):
    def __init__(self, name, floor, head_name, st_name, st_address, st_city, doctors_count):
        super().__init__(st_name, st_address, st_city, doctors_count)
        self.name = name
        self.floor = floor
        self.head_name = head_name


class Doctor(Stomatology):
    def __init__(self, department_name, doctor_name, position, academic_title, experience, st_name, st_address, st_city, doctors_count):
        super().__init__(st_name, st_address, st_city, doctors_count)
        self.department_name = department_name
        self.doctor_name = doctor_name
        self.position = position
        self.academic_title = academic_title
        self.experience = experience


class MedicalHistory(Stomatology):
    def __init__(self, patient_name, insurance_number, treatment_date, services, payment_amount, doctor_name, st_name, st_address, st_city, doctors_count):
        super().__init__(st_name, st_address, st_city, doctors_count)
        self.patient_name = patient_name
        self.insurance_number = insurance_number
        self.treatment_date = treatment_date
        self.services = services
        self.payment_amount = payment_amount
        self.doctor_name = doctor_name

# Создаем экземпляр стоматологической клиники
clinic = Stomatology("лалала", "ул.Западная 10", "Ошмяны", 10)
# Создаем экземпляр отделения
department = Department("Стоматология пумпум", 3, "Иванов Иван Иванович", clinic.name, clinic.address, clinic.city, clinic.doctors_count)
# Создаем экземпляр врача
doctor = Doctor(department.name, "Петров Петр Петрович", "стоматолог", "кандидат медицинских наук", 6, clinic.name, clinic.address, clinic.city, clinic.doctors_count)
# Создаем экземпляр истории болезни пациента
medical_history = MedicalHistory("Иванов Иван Иванович", "1234567890", "21.11.2023", "лечение кариеса", 60, doctor.doctor_name, clinic.name, clinic.address, clinic.city, clinic.doctors_count)
# Вывод информации о созданных экземплярах
print("Информация о стоматологической клинике")
print("Название:", clinic.name)
print("Адрес:", clinic.address)
print("Город:", clinic.city)
print("Количество врачей:", clinic.doctors_count)
print(" Информация об отделении")
print("Название отделения:", department.name)
print("Этаж:", department.floor)
print("ФИО заведующего:", department.head_name)
print("Информация о враче")
print("Название отделения:", doctor.department_name)
print("ФИО врача:", doctor.doctor_name)
print("Должность:", doctor.position)
print("Научное звание:", doctor.academic_title)
print("Стаж работы:", doctor.experience)
print(" Информация об истории болезни пациента")
print("ФИО пациента:", medical_history.patient_name)
print("Номер полиса:", medical_history.insurance_number)
print("Дата лечения:", medical_history.treatment_date)
print("Оказанные услуги:", medical_history.services)
print("Сумма оплаты:", medical_history.payment_amount)
print("ФИО врача:", medical_history.doctor_name)