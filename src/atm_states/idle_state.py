from .atm_state import ATMState
from .has_card_state import HasCardState

# Update IDLE State 
class IdleState(ATMState):
    def insert_card(self, atm, user):
        print("Card is Inserted")
        print(atm)
        print(user)
        atm.set_current_atm_state(HasCardState())
        

# ATMStates
# import ATM
# import Card

# IdleState extends ATMState {
#     public void insertCard(ATM atm, Card card){
#         print(Card is inserted)
#         atm.setCurrentATMState(new HasCardState())
#     }
# }

# ATMState 는 단계 별로 가지고 있음. 
# 만약 IdleState가 실행되지 않았으면 wrong message
# 만약 IdleState가 실행되면 위와 같이 부모 State를 업데이트