class BankAccount:

    def __init__(self, accountNumber , name, balance=0):
        self.ac = int(accountNumber)
        self.name= name
        self.balance = int(balance)

    def deposit(self, depoValue):
        self.balance = self.balance + depoValue
        return print("Balance after deposit", self.balance)

    def withdrawal(self, wdValue):
        self.balance = self.balance - wdValue
        return  self.balance

    def bankFees(self, fees):
        self.fees = fees
        self.balance = self.balance - (fees*self.balance)
        return self.balance

    def display_details(self):
        print(f"Balance is {self.balance}, Name is {self.name} and Account number is {self.ac}")
        print(f"Final balance after fees deduction is {self.balance}")


Bank = BankAccount(12345, "Shivam", 1000)
Bank.display_details()
print(Bank.deposit(200))
print(Bank.withdrawal(100))
print(Bank.bankFees(0.05))