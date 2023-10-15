class User:
    # README: User - Represents a user in our system.
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __str__(self):
        return f'User({self.name}, {self.email})'
