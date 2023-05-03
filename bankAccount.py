# Create a BankAccount class with the attributes interest rate and balance
class bankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!

    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        bankAccount.all_accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    @classmethod
    def get_all_info(cls):
        for account in cls.all_accounts:
            print("Balance: " + str(account.balance) +
                  " Interest Rate: " + str(account.int_rate))
            account.display_account_info()


# Add a deposit method to the bankAccount class


    def deposit(self, amount):
        self.balance += amount
        return self
# Add a withdraw method to the bankAccount class

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
        self.balance -= 5
        return self
# Add a display_account_info method to the bankAccount class

    def display_account_info(self):
        print("Balance: " + str(self.balance))
        return self

# Add a yield_interest method to the bankAccount class
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
            return self


# Create 2 accounts
account1 = bankAccount(.10, 200)  # interest 10% with 200 initial balance
account2 = bankAccount(.05, 100)  # interest 5% with 100 initial balance
bankAccount.get_all_info()
# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)

account1.deposit(100).deposit(300).deposit(1000).withdraw(400).yield_interest().display_account_info()  # Balance: 1314.5

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
account2.deposit(1000).deposit(50).withdraw(20).withdraw(20).withdraw(100).withdraw(100).yield_interest().display_account_info()  # Balance: 934.5

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
account1.get_all_info()
