import unittest

from src import CardReader 

class TestCardReader(unittest.TestCase):
    # Case 1: Card State is active after valid check has been completed
    def test_card_validation(self):
        """
        Test that 12/23 visa card is valid 
        """
        card_info = {"card_type" : "visa", "exp_date" : "12/23"}
        card1 = CardReader()
        
        card1.card_valid_check(card_info)

        self.assertTrue(card1.card_valid_check(card_info))

        """
        Test that 10/22 master card is invalid
        """
        card_info = {"card_type" : "master", "exp_date" : "10/22"}
        card2 = CardReader()
        
        card2.card_valid_check(card_info)

        self.assertFalse(card2.card_valid_check(card_info))

        """
        Test that 12/25 american card is invalid
        """
        card_info = {"card_type" : "american", "exp_date" : "12/25"}
        card3 = CardReader()

        card3.card_valid_check(card_info)

        self.assertFalse(card2.card_valid_check(card_info))

        



if __name__ == "__main__":
    unittest.main()
