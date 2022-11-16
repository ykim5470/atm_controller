from .atm_state import ATMState

class Deposit(ATMState):
    def __init__(self):
        self.deposit_amount = None

    def deposit(self, atm, card):
        self.deposit_amount = int(input("Please enter the deposit amount : "))
        card.add_bank_balance(self.deposit_amount)
        atm.add_atm_balance(self.deposit_amount)
        self.exit(atm)


    def exit(self, atm):
        self.return_card()
        print("Exit happens")


    def return_card(self):
        print("Please collect your card")