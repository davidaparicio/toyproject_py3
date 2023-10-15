class Product:
    # README: Product - Represents a product for sale.
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f'Product({self.name}, ${self.price:.2f})'
        #return f'Product({self.name}, {self.price})'
