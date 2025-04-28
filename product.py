
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def afisare_info(self):
        print(f"Produsul {self.name} are pretul {self.price} si cantitatea {self.quantity}.")

    def actualizare_cantitate(self, new_quantity):
        self.quantity = new_quantity