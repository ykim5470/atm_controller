from .atm_state import ATMState
from .select_operation_state import SelectOperationState

class HasCardState(ATMState):
    def authenticate_pin(self, atm, card, pin):
        is_correct_pin_entered = card.is_correct_pin_entered(pin)

        if(is_correct_pin_entered):
            atm.set_current_atm_state(SelectOperationState())
            print("Authenticated passed")
        else:
            print("Invalid PIN Number")
            self.exit(atm)


    def exit(self, atm):
        self.return_card()
        print("Exit happens")


    def return_card(self):
        print("Please collect your card")