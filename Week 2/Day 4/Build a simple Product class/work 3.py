class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display_info(self):
        print("Book Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        
    def total_price(self):
        return self.price * self.quantity
    

p1 = Product("Book", 5000, 40)

p1.display_info()
print("Total Price:", p1.total_price())