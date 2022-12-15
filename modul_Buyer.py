class Buyer:
    """Створюємо клас Покупець і визначаємо ім'я, прізвище та номер телефону Покупця"""
    def __init__(self, name: str, surname: str, telephon: int):
        self.name = name
        self.surname = surname
        self.telephon = telephon

    def __str__(self):
        """Функція повертає ім'я, прізвище та телефон Покупця"""
        return f'Buyer: {self.name}, {self.surname}, telephon: {self.telephon}'
