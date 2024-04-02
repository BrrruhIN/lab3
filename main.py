from parent_class import Product, Fruits, Vegetables

banana = Fruits("Банан", 0.2)
print("Название продукта:", banana._product_name)
print("Вес:", banana.weight)
print("Цена:", banana.get_price())

potato = Vegetables("Картофель", 1.5)
print("Название продукта:", potato._product_name)
print("Вес:", potato.weight)
print("Цена:", potato.get_price())

