class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display_info(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        
    def total_price(self):
        return self.price * self.quantity
    
p1 = Product("BMW Car", 55000000, 1)


p1.display_info()
print("Total Price:", p1.total_price())