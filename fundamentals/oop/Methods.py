class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

# Creating instances of the User class
guido = User("Guido van Rossum" , "guido@gmail.com")
monty = User ( "Monty Python" , "montly@gmail.com")

# Printing account balances
guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	
print(monty.account_balance)	

