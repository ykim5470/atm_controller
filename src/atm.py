from atm_states import ATMState

from card_reader import CardReader

from atm_states import IdleState



class ATM(ATMState):
    def __init__(self):
        self.temp_card_ROM = None
        self.atm_balance = 0
        self.current_atm_state = ATMState()

    @staticmethod
    def get_atm_object():
        dummy_atm = ATM()
        print("A new ATM has been created")
        print(dummy_atm)
        dummy_atm.set_current_atm_state(IdleState())
        return dummy_atm

    def set_atm_balance(self, max_note):
        self.atm_balance = max_note
    
    def get_atm_balance(self):
        return self.atm_balance

    def print_current_atm_status(self):
        # print("Balance: {self.atm_balance}")
        print("aaa")
        return


    def set_current_atm_state(self, current_atm_state):
        self.current_atm_state = current_atm_state

    def deduct_atm_balance(self, amount):
        self.atm_balance = self.atm_balance - amount
        
    def add_atm_balance(self, amount):
        self.atm_balance = self.atm_balance + amount

    def get_current_atm_state(self):
        return self.current_atm_state

        
    


        
        
