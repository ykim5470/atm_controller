from user_bank_account import BankAccount

from card import Card


class User():
    def __init__(self):
        self.card = None

    def get_card(self):
        return self.card 

    def set_card(self, card):
        self.card = card
        