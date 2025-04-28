
class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product_to_cart(self, name, price, quantity):
        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.cart_items.append(product)
        print(f"{name} a fost adaugat in cos cu pretul {price} si in cantitate de {quantity}.")
    
    def total_payment(self):
        total = 0
        for product in self.cart_items:
            total += product['price'] * product['quantity']
        print(f"Totalul de plata este de {total}.")

    def show_cart_items(self):
        for product in self.cart_items:
            print(f"{product['name']} are pretul de {product['price']} si este prezent in cos in cantitate de {product['quantity']}.")

# cos = Cart()

# cos.add_product_to_cart("Laptop", 2500, 3)
# cos.add_product_to_cart("Monitor", 700, 4)
# cos.add_product_to_cart("Mouse", 100, 20)
# print()
# cos.total_payment()
# print()
# cos.show_cart_items()
