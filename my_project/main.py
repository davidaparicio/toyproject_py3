from models.user import User
from models.product import Product

def main():
    user = User('John Doe', 'john.doe@example.com')
    product = Product('Sample Product', 19.99)
    
    print(user)
    print(product)

if __name__ == "__main__":
    main()
