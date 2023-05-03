from bankAccount import bankAccount


class User:
    def __init__(self, name, email, accountType):
        self.name = name
        self.email = email
        self.account = bankAccount(int_rate=0.02, balance=0)
        # self.bankAccount_Type = ("Checking", "Savings")
# need to figure out how to assign account type to user and create multiple accounts for user

# Add a make_deposit method to the User class that calls on it's bank account's instance methods.


    def make_deposit(self, amount):
        self.account.balance += amount
        return self

# Add a withdraw method to the BankAccount class

    def make_withdraw(self, amount):
        self.account.balance -= amount
        return self

# Add a display_user_balance method to the User class that displays user's account balance

    def display_account_balance(self):
        print("User: " + self.name, "|| Balance: " + str(self.account.balance))
        return self

# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.

    def transfer_money(self, amount, other_user):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self


bigBoss = User("Monty Python", "monty@python.com", "Checking")
account3 = User("Andrew T", "andrew.tran@gmail.com", "Savings")
account3.make_deposit(100000).make_withdraw(700).display_account_balance()
bigBoss.transfer_money(40, account3)

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
