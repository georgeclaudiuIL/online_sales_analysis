
import random
from product_manager import ProductManager
from cart import Cart

product_manager = ProductManager()

product_manager.add_products("Sursa", 2500, 3)
product_manager.add_products("Placa de baza", 700, 4)
product_manager.add_products("Placa video", 100, 20)
print()

product_manager.add_products("Laptop", 2500, 3)
product_manager.add_products("Monitor", 700, 4)
product_manager.add_products("Mouse", 100, 20)
product_manager.add_products("Tastatura", 70, 20)
product_manager.add_products("Carcasa PC", 250, 10)
print()
product_manager.show_products()
print()
product_manager.total_value()
print()

cos = Cart()
produse_random = random.sample(product_manager.products, 3)

# print(produse_random)

for produs in produse_random:
    cos.add_product_to_cart(produs['name'], produs['price'], produs['quantity'])
print()
cos.total_payment()
print()
cos.show_cart_items()
print()
