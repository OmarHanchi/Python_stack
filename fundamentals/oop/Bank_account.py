class Bank_account :
    accounts = []
    def __init__(self,balance=0,interest_rate=0.01) :
        self.interest_rate = interest_rate
        self.balance = balance
        Bank_account.accounts.append(self) 
    # adding the deposit method
    def make_deposit(self, amount):
        self.balance += amount
        return self 
    # adding the withdraw method
    def make_withdrawal (self,amount) :
        if self.balance < amount :
            print ("Insufficient funds: Charging a $5 fee" )
            self.balance -= 5 
        else :           
            self.balance -= amount 
        return self 
    # adding the display_account_info method
    def display_account_info(self) :
        print (f"Balance: ${self.balance}")
    #Adding a yield_interest method 
    def yield_interest (self,):
        if self.balance > 0:
            self.balance += self.balance*self.interest_rate
        return self 
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()
    
# Creating accounts : 
account1= Bank_account (100,0.01)
account2=Bank_account (200,0.02)
account1.make_deposit(50).make_deposit(100).make_deposit(150).make_withdrawal(100).yield_interest().display_account_info()
account2.make_deposit(400).make_deposit(300).make_withdrawal(50).make_withdrawal(175).make_withdrawal(100).make_withdrawal(300).yield_interest().display_account_info()
Bank_account.print_all_accounts()