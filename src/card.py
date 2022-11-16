
class Card():
    _card_number = "1234567891234"
    _cvv = "000"
    _exp_date = "12/23"
    _card_type = "visa"
    _holder_name = "Lewis"
    _pin_number = 6789
    _bank_account = None

    def __init__(self):
        _bank_account = None

    def is_correct_pin_entered(self, pin):
        if(pin == self._pin_number):
            return True
        return False 
    
    def get_bank_balance(self):
        return self._bank_account.balance
    
    def deduct_bank_balance(self, amount):
        self._bank_account.with_draw_balance(amount)
        
    def add_bank_balance(self, amount):
        self._bank_account.with_deposit_balance(amount)

    def set_bank_account(self, bank_account):
        self._bank_account = bank_account