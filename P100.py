import random
class ATM(object):
    def __init__(self,card_number,pin,type):
        self.card_number=card_number
        self.pin=pin
        self.type=type
    
    def cashWithdrawl(self):
        print("Cash Withdrawn")

    def amount(self):
        amt=input("How much you want to withdraw? ")
        print(amt)
        print("withdrawn")
    
    def account(self):
        print("Your account has-$")
        acc=random.randint(1000,9000)
        print(acc)
    
    def withdrawl_type(self):
        print("You are taking from your savings account")

card1=ATM("12454456754","3467","debit")
print(card1.amount)