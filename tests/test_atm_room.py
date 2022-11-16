import unittest

from src.atm_room import ATMRoom 

class TestAtmRoom(unittest.TestCase):
    # Case 1: atm instance is initiated after _initialize() 
    def test_atm_initialize(self):
        """
        Test that a new instance has been created successfully
        """
        new_atm = ATMRoom()
        new_atm._initialize()

        self.assertNotEqual(new_atm.atm, None)
        self.assertNotEqual(new_atm.user, None)
        self.assertNotEqual(new_atm.transaction, None)

        """
        Test that card insert motion detected from atm 
        """
        new_atm = ATMRoom()
        new_atm._initialize()
        new_atm.atm.print_current_atm_status()
        new_atm.atm.get_current_atm_state().insert_card(new_atm.atm, new_atm.user.card)

        self.assertEqual(new_atm.atm.insert_card(new_atm.atm, new_atm.user.card), "error")
        

        """
        Test that pin number is valid or not
        """
        new_atm = ATMRoom()
        new_atm._initialize()
        new_atm.atm.print_current_atm_status()
        new_atm.atm.get_current_atm_state().insert_card(new_atm.atm, new_atm.user.card)
        new_atm.atm.get_current_atm_state().authenticate_pin(new_atm.atm, new_atm.user.card, 6789)

        



        

        """
        Test that 12/25 american card is invalid
        """


        



if __name__ == "__main__":
    unittest.main()
