class Person:
    """Створюємо клас Людина: им'я, по-батькові, прізвище, вік"""

    def __init__(self, name: str, second_name: str, surname: str, age: int):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.age = age

    def print_name(self):
        """Функція виведення ПІБ особи"""
        return f'{self.name} {self.second_name} {self.surname}'

    def print_age(self):
        """Функція виведення віку особи"""
        return f'Age: {self.age} years old'

    def __str__(self):
        """Функція виведення загального опису особи"""
        return f'{self.name} {self.second_name} {self.surname}, age: {self.age} years old'
