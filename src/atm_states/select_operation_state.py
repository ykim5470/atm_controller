from .atm_state import ATMState
from transaction_type import TransactionType
from .card_with_draw_state import Withdraw
from .check_balance_state import Balance
from .deposit_cash_state import Deposit


class SelectOperationState(ATMState):
    
    def select_operation(self, atm, card, type):
        match type:
            case 1:
                print("Deposit selected")
                atm.set_current_atm_state(Deposit().deposit(atm, card))
            case 2:
                print("Withdraw selected")
                atm.set_current_atm_state(Withdraw().withdraw(atm, card))
            case 3:
                print("Balance selected")
                atm.set_current_atm_state(Balance().balance(atm, card))
            case 4:
                self.exit(atm)
            case _:
                print("Invalid Option")
                self.exit(atm)
        

    def exit(self, atm):
        self.return_card()
        print("Exit happens")

    def return_card(self):
        print("Please collect your card")
    