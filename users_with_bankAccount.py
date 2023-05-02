from bankAccount import bankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = bankAccount(int_rate=0.02, balance=0)

    # other methods

# Add a make_deposit method to the User class that calls on it's bank account's instance methods.

    def make_deposit(self, amount):
        self.account.balance += amount
        return self

# Add a withdraw method to the BankAccount class

    def make_withdraw(self, amount):
        self.account.balance -= amount
        if self.account.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
        self.account.balance -= 5
        return self.account.balance

# Add a display_user_balance method to the User class that displays user's account balance

    def display_account_balance(self):
        print(self.account.balance)
        return self

account3 = User("Andrew", "Andrew@Tran.com")
account3.make_deposit(100000).make_deposit(100000).display_account_balance()