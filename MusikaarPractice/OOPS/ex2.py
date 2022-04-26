class Bank:
    def deposit(self, balance, amount):
        return balance + amount

    def withdraw(self, balance, amount):
        if amount > balance:
            print("Saaale Garib")
        else:
            return balance - amount

    def view_balance(self, balance):
        return balance


bal = 10000
piggy_bank = Bank()
while True:

    print("Balance is", piggy_bank.view_balance(bal))
    # ask for deposit/withdraw

    operation_type = input("Deposit OR Withdraw? Type d for Deposit OR w for Withdraw OR e for Exit: ")

    if operation_type == "d" or operation_type == "D":
        amount_deposit = int(input("Enter amount for deposit: "))
        bal = piggy_bank.deposit(bal, amount_deposit)
        print(f"Deposited {amount_deposit} and Total balance is {bal} ")
    elif operation_type == "w" or operation_type == "W":
        amount_withdraw = int(input("Enter amount for withdraw: "))
        bal = piggy_bank.withdraw(bal, amount_withdraw)
        print(f"Withdrew {amount_withdraw} and Total balance is {bal} ")
    elif operation_type == "e" or operation_type == "E":
        break
    else:
        print("Invalid operation type")



