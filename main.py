class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

        else:
            print("Sorry not sufficient account balance!")

    def statement(self):
        print("Current Balance is $ {}".format(self.balance))


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        return "{}'s Current Account, Balance: {}".format(self.name, self.balance)


class Savings(Account):
    def __init__(self,name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return "{}'s Savings Account, Balance: {}".format(self.name, self.balance)


person = Current("Shreyash Lamkane", 5000000)
person.statement()
person.withdraw(45000)
person.statement()
print(person)

person2=Savings("John Cena", 6000000)

print(person2)
person2.withdraw(65000)
person2.deposit(30000)
person2.statement()

