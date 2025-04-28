
class ProductManager:
    def __init__(self):
        self.products = []

    def add_products(self, name, price, quantity):
        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            print(f"Produsul {product['name']} cu pretul {product['price']} este prezent in cantitate de {product['quantity']}.")

    def total_value(self):
        total = 0
        for product in self.products:
            total += product['price'] * product['quantity']
        print(f"Valoarea totala a produselor este {total}.")

# lista_produse = ProductManager()
# print()
# lista_produse.add_products("Laptop", 2500, 3)
# lista_produse.add_products("Monitor", 700, 4)
# lista_produse.show_products()
# print()
# lista_produse.total_value()
# print()