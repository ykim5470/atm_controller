class BankAccount():
    def __init__(self):
        self.name = None
        self.balance = None 

    def with_draw_balance(self, amount):
        self.balance = self.balance - amount 

    def with_deposit_balance(self, amount):
        self.balance = self.balance + amount