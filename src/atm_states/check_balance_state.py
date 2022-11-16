from .atm_state import ATMState

class Balance(ATMState):
    def __init__(self):
        pass
        
    def balance(self, atm, card):
        print(f"Your Account Balance is: {card.get_bank_balance()}")
        self.exit(atm)


    def exit(self, atm):
        self.return_card()
        print("Exit happens")


    def return_card(self):
        print("Please collect your card")
    