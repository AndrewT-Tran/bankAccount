# Create a BankAccount class with the attributes interest rate and balance
class BankAccount:

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
# Add a deposit method to the BankAccount class

    def deposit(self, amount):
        self.balance += amount
        return self
# Add a withdraw method to the BankAccount class

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
        self.balance -= 5
        return self
# Add a display_account_info method to the BankAccount class

    def display_account_info(self):
        print(self.balance)
        return self

# Add a yield_interest method to the BankAccount class
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
            return self


# Create 2 accounts
account1 = BankAccount(.10, 200)  # interest 10% with 200 initial balance
account2 = BankAccount(.05, 100)  # interest 5% with 100 initial balance

#To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)

account1.deposit(100).deposit(300).deposit(1000).withdraw(400).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)

account2.deposit(1000).deposit(50).withdraw(20).withdraw(20).withdraw(100).withdraw(100).yield_interest().display_account_info()

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
# @classmethod
# def get_all_info(cls):
#     for account in cls.all_accounts:
#         account.display_account_info()
#     print(account.display_account_info())
# account1.get_all_info()