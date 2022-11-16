from user import User 
from card import Card
from user_bank_account import BankAccount
from transaction_type import TransactionType
from atm import ATM
        

# from card import Card
class ATMRoom():
    def __init__(self):
        self.atm = None
        self.user = None 
        self.transaction = None

    # Init atm system 
    def _initialize(self):
        # Create ATM object 
        self.atm = ATM.get_atm_object()

        # Set atm max notes
        self.atm.set_atm_balance(3500)

        # Create User 
        self.user = self._create_user() 

        # Create Transaction options 
        self.transaction = self._create_options()


    def _create_user(self):
        dummy_user = User()
        dummy_user.set_card(self._create_card())
        return dummy_user 

    def _create_card(self):
        dummy_card = Card()
        dummy_card.set_bank_account(self._create_bank_account())
        return dummy_card

    def _create_bank_account(self):
        dummy_bank_account = BankAccount()
        dummy_bank_account.balance = 3000

        return dummy_bank_account

    def _create_options(self):
        dummy_options = TransactionType("withdraw", "balance", "deposit")
        return dummy_options

    


if __name__ == "__main__":
    new_atm = ATMRoom()
    new_atm._initialize()
    

    new_atm.atm.print_current_atm_status()
    new_atm.atm.get_current_atm_state().insert_card(new_atm.atm, new_atm.user.card)
    new_atm.atm.get_current_atm_state().authenticate_pin(new_atm.atm, new_atm.user.card, 6789)
    new_atm.atm.get_current_atm_state().select_operation(new_atm.atm, new_atm.user.card, new_atm.transaction.show_all_transaction_types())
    # new_atm.atm.get_current_atm_state().withdraw(new_atm.atm, new_atm.user.card, 2700)
    # new_atm.atm.get_current_atm_state().balance(new_atm.atm, new_atm.user.card)
    new_atm.atm.print_current_atm_status()
