class Product:
    def __init__(self, product_name, weight):
        self._product_name = product_name
        self.weight = weight

    def get_price(self):
        print("Parent method")

class Fruits(Product):
    def get_price(self):
        super().get_price()
        return self.weight * 100

class Vegetables(Product):
    def get_price(self):
        super().get_price()
        return self.weight * 50
