import unittest
from user_create import UserCreation

class TestUserCreation(unittest.TestCase):

    def test_first_name_generation(self):
        self.assertTrue(UserCreation.generate_first_name() == "Rick") 

    def test_last_name_generation(self):
        self.assertTrue(UserCreation.generate_last_name() == "Deckard") 

    if __name__ == "__main__":
        unittest.main()
