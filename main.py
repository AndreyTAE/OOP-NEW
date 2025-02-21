class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # Дополнительные атрибуты для лекторов могут быть добавлены здесь


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # Дополнительные атрибуты для экспертов могут быть добавлены здесь


# Пример использования
best_student = Student("Ruoy", "Eman", "your_gender")
best_student.courses_in_progress += ["Python"]

cool_lecturer = Lecturer("Some", "Buddy")
cool_lecturer.courses_attached += ["Python"]

cool_reviewer = Reviewer("John", "Doe")
cool_reviewer.courses_attached += ["Python"]

cool_lecturer.rate_hw(best_student, "Python", 10)
cool_lecturer.rate_hw(best_student, "Python", 10)
cool_lecturer.rate_hw(best_student, "Python", 10)

print(best_student.grades)
