
class Product:
    def __init__(self):
        self.id = None
        self.name = None
        self.price = None

    def set(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.id} {self.name} {self.price}'
