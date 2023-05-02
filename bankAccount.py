class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
        self.balance -= 5
        return self

    def display_account_info(self):
        print(self.balance)

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
            return self


account1 = BankAccount(.10, 200)  # interest 10% with 200 initial balance
account2 = BankAccount(.05, 100)  # interest 5% with 100 initial balance

account1.deposit(100).withdraw(400).deposit(1000).display_account_info()
account2.yield_interest().display_account_info()
