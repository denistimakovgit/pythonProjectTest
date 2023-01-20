class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lector, course, grade):
        if int(grade) in range(0, 11) and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avr_rating_st(self):
        self.rates = []
        if len(self.grades) != 0:
            for key, value in self.grades.items():
                for elem in value:
                    self.rates.append(elem)
            self.avr_res = sum(self.rates) / len(self.rates)
            return self.avr_res
        else:
            return 'Оценок нет'

    def __str__(self):
        mean_studetn_value = self.avr_rating_st()
        str_courses = ', '.join(self.courses_in_progress)
        str_finished_courses = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {mean_studetn_value}' \
              f'\nКурсы в процессе изучения: {str_courses}\n' \
              f'Завершенные курсы: {str_finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.avr_rating_st() < other.avr_rating_st()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avr_rating(self):
        self.rates = []
        if len(self.grades) != 0:
            for key, value in self.grades.items():
                for elem in value:
                    self.rates.append(elem)
            self.avr_res = sum(self.rates) / len(self.rates)
            return self.avr_res
        else:
            return 'Оценок нет'

    def __str__(self):
        mean_v = self.avr_rating()
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {mean_v}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Mentor')
            return
        return self.avr_rating() < other.avr_rating()

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def avr_all_students(list_of_students, name_of_course):
    """
    Функция для подсчета средней оценки за домашние задания по всем студентам
    в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
    """
    dict_of_students = {}
    total_marks = []
    for elem in list_of_students:
        dict_of_students.update(elem.grades)
        if name_of_course in dict_of_students:
            total_marks.append(dict_of_students[name_of_course])
        dict_of_students.clear()
    m_total_marks = sum(total_marks, []) #распаковываем список в единый список оценок
    res = sum(m_total_marks)/len(m_total_marks)
    print(f'Средняя оценка за ДЗ по курсу {name_of_course}: {res}')

def avr_all_lectors(list_of_lectors, name_of_course):
    """
    Функция для подсчета средней оценки за лекции всех лекторов
    в рамках курса (в качестве аргумента принимаем список лекторов и название курса)
    """
    dict_of_lectors = {}
    total_marks = []
    for elem in list_of_lectors:
        dict_of_lectors.update(elem.grades)
        if name_of_course in dict_of_lectors:
            total_marks.append(dict_of_lectors[name_of_course])
        dict_of_lectors.clear()
    m_total_marks = sum(total_marks, []) #распаковываем список в единый список оценок
    res = sum(m_total_marks)/len(m_total_marks)
    print(f'Средняя оценка за лекцию по курсу {name_of_course}: {res}')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

bad_student = Student('Bart', 'Simpson', 'man')
bad_student.courses_in_progress += ['Java']
bad_student.finished_courses += ['Введение в программирование']

# третьего студента создаем для проверки функции подсчета ср.оценки за курс Python
py_student = Student('Homer', 'Simpson', 'man')
py_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

main_rewiever = Reviewer('Snoop','Dog')
main_rewiever.courses_attached += ['Python']
main_rewiever.rate_hw(best_student, 'Python', 10)
main_rewiever.rate_hw(best_student, 'Python', 10)
main_rewiever.rate_hw(best_student, 'Python', 10)

main_rewiever.rate_hw(py_student, 'Python', 9)
main_rewiever.rate_hw(py_student, 'Python', 9)

second_reviewer = Reviewer('Curtis', 'Jackson')
second_reviewer.courses_attached += ['Java']
second_reviewer.rate_hw(bad_student, 'Java', 3)
second_reviewer.rate_hw(bad_student, 'Java', 3)
second_reviewer.rate_hw(bad_student, 'Java', 3)

first_lecturer = Lecturer('Conor','McGregor')
best_student.rate_lecturer(first_lecturer, 'Python', 8)
best_student.rate_lecturer(first_lecturer, 'Python', 8)

second_lecturer = Lecturer('Jose','Aldo')
bad_student.rate_lecturer(second_lecturer, 'Java', 4)
bad_student.rate_lecturer(second_lecturer, 'Java', 4)

print(main_rewiever)
print(second_reviewer)
print(first_lecturer)
print(second_lecturer)
print(best_student)
print(bad_student)
print('Сравнение лекторов:')
print(first_lecturer > second_lecturer)
print('Сравнение студентов:')
print(best_student > bad_student)

# подсчет ср.оценки за ДЗ по всем студентам в рамках конкретного курса
avr_all_students([best_student, bad_student, py_student], 'Python')

# подсчет ср.оценки за лекции по всем преподавателям в рамках конкретного курса
avr_all_lectors([first_lecturer, second_lecturer], 'Python')