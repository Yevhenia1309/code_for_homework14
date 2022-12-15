import Modul_Person

class Student(Modul_Person.Person):
    """На базі класу Людина створюємо клас Студент: додаємо назву університету і факультету"""
    def __init__(self, name, second_name, surname, age, university: str, faculty: str):
        super().__init__(name, second_name, surname, age)
        self.university = university
        self.faculty = faculty

    def print_university(self):
        """Функція виведення університету, де навчається студент"""
        return f'University: {self.university}'

    def print_faculty(self):
        """Функція виведення факультету, де навчається студент"""
        return f'Faculty: {self.faculty}'

    def __str__(self):
        """Функція виведення загального опису студента"""
        return "Student: " + super().__str__() + ',' + " university is {}, faculty is {}".format(self.university,\
                                                                                                 self.faculty)
