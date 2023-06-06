class BankAccount:
    all_accounts = []

    # don't forget to add some default values for these parameters!

    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    @classmethod
    def get_all_info(cls):
        for account in cls.all_accounts:
            print(
                "Balance: "
                + str(account.balance)
                + " Interest Rate: "
                + str(account.int_rate)
            )
            account.display_account_info()

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.int_rate / 100)
        return self


Andrew = BankAccount(0.5, 100)
Emily = BankAccount(0.5, 1000)
Andrew.deposit(41).deposit(100).deposit(2000).withdraw(
    200
).yield_interest().display_account_info()
Emily.deposit(100).deposit(40).withdraw(20).withdraw(20).withdraw(20).withdraw(
    30
).yield_interest().display_account_info()

print("-------------------")
BankAccount.get_all_info()