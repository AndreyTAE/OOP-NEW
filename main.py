class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.lecturer_grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if lecturer.name in self.lecturer_grades:
                self.lecturer_grades[lecturer.name].setdefault(course,[]).append(grade)
            else:
                self.lecturer_grades[lecturer.name] = {course: [grade]}
        else:
            return "Ошибка"

    def __str__(self):
        average_grade = 0
        course_count = 0
        for course, grades in self.grades.items():
            average_grade += sum(grades) / len(grades)
            course_count +=1
        if course_count > 0:
            average_grade /= course_count
        else:
            average_grade = 0

        courses_in_progress_str = ", ".join(self.courses_in_progress) or "Нет курсов в процессе изучения"
        finished_courses_str = ", ".join(self.finished_courses) or "Нет завершенных курсов"
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade:.1f}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}"

    def __lt__(self, other):
        average_grade_self = 0
        course_count_self = 0
        for course, grades in self.grades.items():
            average_grade_self += sum(grades) / len(grades)
            course_count_self += 1
        if course_count_self > 0:
            average_grade_self /= course_count_self
        else:
            average_grade_self = 0

        average_grade_other = 0
        course_count_other = 0
        for course, grades in other.grades.items():
            average_grade_other += sum(grades) / len(grades)
            course_count_other += 1
        if course_count_other > 0:
            average_grade_other /= course_count_other
        else:
            average_grade_other = 0

        return average_grade_self < average_grade_other


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        average_grade = 0
        course_count = 0
        for course, grades in self.grades.items():
            average_grade += sum(grades) / len(grades)
            course_count += 1
        if course_count > 0:
            average_grade /= course_count
        else:
            average_grade = 0
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}"

    def __lt__(self, other):
        average_grade_self = 0
        course_count_self = 0
        for course, grades in self.grades.items():
            average_grade_self += sum(grades) / len(grades)
            course_count_self += 1
        if course_count_self > 0:
            average_grade_self /= course_count_self
        else:
            average_grade_self = 0

        average_grade_other = 0
        course_count_other = 0
        for course, grades in other.grades.items():
            average_grade_other += sum(grades) / len(grades)
            course_count_other += 1
        if course_count_other > 0:
            average_grade_other /= course_count_other
        else:
            average_grade_other = 0

        return average_grade_self < average_grade_other


def average_grade_students(students, course):
    total_grade = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course]) / len(student.grades[course])
            count += 1
    return total_grade / count if count else 0


def average_grade_lecturers(lecturers, course):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grade += sum(lecturer.grades[course]) / len(lecturer.grades[course])
            count += 1
    return total_grade / count if count else 0


best_student = Student("Ruoy", "Eman", "male")
best_student.courses_in_progress += ["Python", "Git"]
best_student.finished_courses += ["Введение в программирование"]

another_student = Student("John", "Doe", "male")
another_student.courses_in_progress += ["Python"]

cool_mentor = Reviewer("Some", "Buddy")
cool_mentor.courses_attached += ["Python", "Git"]

cool_lecturer = Lecturer("Super", "Lecturer")
cool_lecturer.courses_attached += ["Python"]

another_lecturer = Lecturer("Another", "Lecturer")
another_lecturer.courses_attached += ["Git"]

cool_mentor.rate_hw(best_student, "Python", 10)
cool_mentor.rate_hw(best_student, "Python", 9)
cool_mentor.rate_hw(best_student, "Git", 8)
cool_mentor.rate_hw(another_student, "Python", 7)

best_student.rate_lecturer(cool_lecturer, "Python", 10)
best_student.rate_lecturer(cool_lecturer, "Python", 9)
another_student.rate_lecturer(cool_lecturer, "Python", 8)
best_student.rate_lecturer(another_lecturer, "Git", 7)


print(best_student)
print(another_student)
print(cool_mentor)
print(cool_lecturer)
print(another_lecturer)

print(f"Средняя оценка студентов по Python: {average_grade_students([best_student, another_student], 'Python')}")
print(f"Средняя оценка лекторов по Python: {average_grade_lecturers([cool_lecturer, another_lecturer], 'Python')}")

print(best_student < another_student)
print(cool_lecturer < another_lecturer)
