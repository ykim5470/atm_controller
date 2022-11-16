from datetime import date, datetime

# Card Reader 
class CardReader():
    global valid_card_date 
    global valid_card_type

    def card_valid_check(self, card_info):
        # Card date & type check
        i1 = self._card_type_check(card_info["card_type"])
        i2 = self._card_date_check(card_info["exp_date"])
        if(i1 & i2):
            return True
        else:
            return False

    def _card_type_check(self, card_type):
        valid_card_type = ["visa", "master"]
        type_validity = True if card_type in valid_card_type else False
        return type_validity  
    
    def _card_date_check(self, exp_date):
        today = date.today()
        exp_date = datetime.strptime(exp_date, "%m/%y")
        m_y_today = today.strftime("%m/%y")
        valid_card_date = datetime.strptime(m_y_today, "%m/%y")

        date_validity =  True if exp_date > valid_card_date else False
        return date_validity

if __name__ == "__main__":
    current_card = CardReader()
    card_info = {"card_type" : "visa", "exp_date" : "12/23"}
    print(current_card.card_valid_check(card_info))