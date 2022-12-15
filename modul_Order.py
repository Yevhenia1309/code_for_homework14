class Order:
    """Створюємо клас Замовлення, визначаємо найменування, список замовлень та загальну вартість"""
    def __init__(self, title: str):
        self.title = title
        self.order = []
        self.total_amount = []

    def add_order(self, good):
        if good not in self.order:
            self.order.append(good)
            self.total_amount.append(good.price)

    def __str__(self):
        return f"{self.title}\n{'^' * 10}\n" + '\n'.join(map(str, self.order)) + '\n' + \
               'Total: ' + f'{sum(map(int, self.total_amount))}' + ' UAH' + '\n'
