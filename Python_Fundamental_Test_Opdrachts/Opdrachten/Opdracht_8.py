class BankAccount(object):

    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('NOT ALLOWED: depositing non-positive amount')
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('NOT ALLOWED: withdrawal non-positive amount')
        if self.balance < amount:
            raise ValueError('NOT ALLOWED: withdrawal exceeds balance')
        self.balance -= amount
        return self.balance


account = BankAccount("Alex")
print(account.owner)
print(account.balance)

try:
    print(account.deposit(10))
except ValueError as ve:
    print(ve)

try:
    print(account.withdraw(3))
except ValueError as ve:
    print(ve)

try:
    print(account.withdraw(30))
except ValueError as ve:
    print(ve)

try:
    print(account.deposit(-12))
except ValueError as ve:
    print(ve)
