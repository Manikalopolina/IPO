class Student:# Объявление класса Student.
    def __init__(self, surname, groupNumber, performance):# Определение конструктора __init__, который принимает параметры surname, groupNumber
        # и performance и инициализирует атрибуты объекта класса.
        self.surname = surname
        self.groupNumber = groupNumber
        self.performance = performance

students = []# Создание пустого списка students.
# Ввод данных с клавиатуры
for i in range(5):# Начало цикла for, который повторяется 5 раз
    print(f"Введите данные для студента {i+1}:")#  Вывод сообщения с просьбой ввести данные о студенте
    surname = input("Введите фамилию и инициалы: ")# Ввод фамилии и инициалов студента с клавиатуры
    groupNumber = input("Введите номер группы: ")# Ввод фамилии и инициалов студента с клавиатуры
    performance = list(map(int, input('Введите оценки студента:').split()))#  Ввод оценок студента с клавиатуры, разделенных пробелом,
    # и преобразование их в список целых чисел.
    students.append(Student(surname, groupNumber, performance))#  Создание объекта класса Student с введенными данными и добавление его в список students
# Проверка студентов с неудовлетворительной успеваемостью
StudentsWithBadPerformance = any(any(mark < 4 for mark in student.performance) for student in students)# . Проверка студентов с
# неудовлетворительной успеваемостью.
# Вывод сообщения, если нет студентов с неудовлетворительной успеваемостью
if StudentsWithBadPerformance:
    print("Студенты с неудовлетворительной успеваемостью:")
    for student in students:#  В цикле for проходятся все студенты в списке students.
        if any(mark < 4 for mark in student.performance):#  Если у студента есть неудовлетворительные оценки, выводится
            # сообщение с его фамилией, инициалами и номером группы.
            print(f"Студент {student.surname}, {student.groupNumber} имеет неудовлетворительную оценку.")
else:# Если нет студентов с неудовлетворительной успеваемостью, выводится сообщение "Нет студентов с неудовлетворительной успеваемостью."
    print("Нет студентов с неудовлетворительной успеваемостью.")