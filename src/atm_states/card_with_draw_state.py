from .atm_state import ATMState

class Withdraw(ATMState):
    def __init__(self):
        self.withdraw_amount = None

    def withdraw(self, atm, card):
        self.withdraw_amount = int(input("Please enter the withdrawal amount : "))

        if atm.get_atm_balance() < self.withdraw_amount:
            print("Insufficient fund in the ATM mathine")
        elif card.get_bank_balance() < self.withdraw_amount:
            print("Insufficient fund in the your Bank Account")
        else:
            card.deduct_bank_balance(self.withdraw_amount)
            atm.deduct_atm_balance(self.withdraw_amount)
            self.exit(atm)


    def exit(self, atm):
        self.return_card()
        print("Exit happens")


    def return_card(self):
        print("Please collect your card")