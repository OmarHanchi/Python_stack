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
        return self.balance 
    #Adding a yield_interest method 
    def yield_interest (self,):
        if self.balance > 0:
            self.balance += self.balance*self.interest_rate
        return self 
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()
    

class User :
    def __init__(self,name) :
        self.name=name
        self.account = {
            "main_account" : Bank_account(0, 0.02),
            "savings" : Bank_account(0,0.05)
        }

    def display_user_balance(self):
        #displays the user balance 
        print (f"user : {self.name} , main account balance : {self.account['main_account'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self
    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self
# Creating accounts : 
omar = User("Omar")
omar.account['main_account'].make_deposit(100)
omar.account['savings'].make_deposit(50)
omar.display_user_balance()
