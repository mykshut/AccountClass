class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, "r") as file:
            self.balance = int(file.read())

    def deposit(self, amount):
        self.balance += amount
        account.commit()
        return (f"The new value on your balance > {self.balance} <")

    def withdraw(self, amount):
        self.balance -= amount
        account.commit()
        return (f"The new value on your balance > {self.balance} <")

    def commit(self):
        with open(self.filepath, "w") as file:
            file.write(str(self.balance))

account = Account("balance.txt")
print(account.balance)
