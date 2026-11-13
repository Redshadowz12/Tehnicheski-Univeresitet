class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, ammount):
        self.balance += ammount
    def withdraw(self, ammount):
        if ammount <= self.balance:
            self.balance -= ammount
        else:
            print("Not enough money")
    def print(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        self.balance += self.interest_rate * self.balance / 100
    def print(self):
        print(f"Owner: {self.owner}, Interest rate: {self.interest_rate}, Balance: {self.balance}")

print("--- Стандартна сметка ---")
acc = Account("Иван Иванов", 1000)
acc.print()

acc.deposit(500)
print("След депозит 500:")
acc.print()

print("Опит за теглене на 1600:")
acc.withdraw(1600)
acc.withdraw(200)
print("След успешно теглене на 200:")
acc.print()

print("\n--- Спестовна сметка ---")
savings = SavingsAccount("Петър Петров", 2000, 5)
savings.print()

savings.add_interest()
print("След добавяне на годишната лихва:")
savings.print()
