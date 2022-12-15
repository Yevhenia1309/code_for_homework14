class Goods:
    """Створюємо клас Товари, визначаємо назву товару, ціну та вагу"""
    def __init__(self, name: str, price: int, weight: int):
        self.name = name
        self.price = price
        self.weight = weight

        if price <= 0:
            raise LimitPriceError(price)

    def __str__(self):
        """Функція повертає назву, ціну та вагу Товару"""
        return f'Goods: {self.name}, price: {self.price} UAH, weight: {self.weight} g'
