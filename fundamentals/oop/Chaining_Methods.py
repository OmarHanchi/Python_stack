class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email 
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self,amount) : 
        #  Adds the specified amount to the account balance.
        self.account_balance += amount 
        return self
    # adding the make withdrawal method
    def make_withdrawal(self,amount):
        #  Subtracts the specified amount from the account balance.
        self.account_balance -= amount
        return self
    # adding the display user balance  method
    def display_user_balance(self):
        #displays the user balance 
        print (self.account_balance)
        return self
    # adding the display user balance  method for the Payment Receipt and Invoice
    def display_user_balance_after_transfer(self):
        #displays the user balance 
        return self
    #adding transfer method
    def transfer_this_amount (self,amount,destination):
        self.make_withdrawal (amount)
        destination.make_deposit (amount )
        print(f"sender : {self.name} / amount : {amount} / reciever : {destination.name}")
        print(f"{self.name} current balance =  {self.display_user_balance_after_transfer()}")
        print(f"{destination.name} current balance = {destination.display_user_balance_after_transfer()}")



# Creating instances of the User class
omar = User ("Omar Hanchi", "omar@gmail.com")
ala = User ("Ala coding " , "ala@gmail.com")
koussay = User ("Koussay coding" , "koussay@gmail.com" )

omar.make_deposit(50).make_deposit(100).make_deposit(150).make_deposit(200).display_user_balance()
ala.make_deposit(200).make_deposit(150).make_withdrawal(150).make_withdrawal(50).display_user_balance()
koussay.make_deposit(400).make_withdrawal(200).make_withdrawal(100).make_withdrawal(50).display_user_balance()

omar.transfer_this_amount(25,ala)