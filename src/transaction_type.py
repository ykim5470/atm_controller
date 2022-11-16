class TransactionType():
    def __init__(self, withdraw, balance, deposit):
        self.withdraw = withdraw 
        self.balance = balance
        self.deposit = deposit


    def show_all_transaction_types(self):
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Balance")
            print("4. Exit")
            option = int(input("Please choose from one of the following options : "))

            return option
