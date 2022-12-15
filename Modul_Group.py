import Modul_Student

class Group:
    """Створюємо клас група студентів,
    встановлюємо максимальний розмір групи"""

    def __init__(self, title: str, max_students: int = 10):
        self.title = title
        self.list_students = []
        self.max_students = max_students

    def add_student(self, student: Modul_Student.Student):
        """Функція додавання студентів з перевіркою чи є вже такий студент у групі і чи є ще місце в групі"""
        if student in self.list_students:
            raise AmountStudentError(student, self.title)
        if len(self.list_students) >= self.max_students:
            raise LimitGroupError(self.max_students)

        self.list_students.append(student)

    def delete_student(self, student: Modul_Student.Student):
        """Функція видалення студента з групи"""
        if student in self.list_students:
            self.list_students.remove(student)

    def find_student(self, surname: str):
        """Функція пошуку студента за прізвищем і додавання у список"""
        res = []
        for student in self.list_students:
            if student.surname == surname:
                res.append(student)
        return res

    def __str__(self):
        """Функція виведення групи студентів"""
        return f"{self.title}\n{'^' * 13}\n" + '\n'.join(map(str, self.list_students)) + '\n'
