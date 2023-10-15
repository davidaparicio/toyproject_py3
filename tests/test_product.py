import unittest
from my_project.models.product import Product

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        product = Product('Sample Product', 19.99)
        self.assertEqual(product.name, 'Sample Product')
        self.assertEqual(product.price, 19.99)

if __name__ == "__main__":
    unittest.main()
