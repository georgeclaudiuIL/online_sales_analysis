
from product_manager import ProductManager

product_manager = ProductManager()

product_manager.add_products("Laptop", 2500, 3)
product_manager.add_products("Monitor", 700, 4)
product_manager.add_products("Mouse", 100, 20)
print()
product_manager.show_products()
print()
product_manager.total_value()
print()