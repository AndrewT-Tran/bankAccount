from bankAccount import bankAccount


class User:
    def __init__(self, name, email, accountType = "Checking"):
        self.name = name
        self.email = email
        self.account = bankAccount(int_rate=0.02, balance=0)
        self.accountType = accountType


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

class UserSaving(bankAccount):
    def __init__(self, name, email, accountType="Savings"):
        super().__init__(name, email)
        self.accountType = accountType

    def make_deposit(self, amount, accountType):
        if accountType == "Savings":
            self.account.balance += amount
            return self
        else:
            super().make_deposit(self, amount)
    def make_withdraw(self, amount, accountType):
        if accountType == " ":
            print("Please specify account type")
        elif accountType == "Savings":
            self.account.balance -= amount
            return self
        else:
            super().make_withdraw(self, amount)



bigBoss = User("Monty Python", "monty@python.com", "Checking")
account3 = User("Andrew T", "andrew.tran@gmail.com", "Checking")
Drew = UserSaving("Andrew T", "drew@drew.com", "Savings")
Drew2 = User("Andrew T", "drew.drew.com", "Checking")
print(Drew.accountType)
print(Drew2.accountType) #need to see if tehre is a way that drew and drew2 are the same user but have different account types
account3.make_deposit(100000).make_withdraw(700).display_account_balance()
bigBoss.transfer_money(40, account3)

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
