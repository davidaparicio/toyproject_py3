import unittest
from my_project.models.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User('John Doe', 'john.doe@example.com')
        self.assertEqual(user.name, 'John Doe')
        self.assertEqual(user.email, 'john.doe@example.com')

if __name__ == "__main__":
    unittest.main()
