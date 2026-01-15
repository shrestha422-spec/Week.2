class Product:
    def __init__(self, name, price, top_speed):
        self.name = name
        self.price = price
        self.top_speed = top_speed
        
    def display_info(self):
        print("Bike Name:", self.name)
        print("Price:", self.price)
        print("Top speed:", self.top_speed)
        
        
p1 = Product("BMW", 5485079, 305)

p1.display_info()