#OOP
class Bank:
    def __init__(self, acc_number,name,bal=500.0):
        self.acc_number = acc_number
        self.name = name
        self.bal = bal

    def deposit(self,amount):
        if amount > 0:
            self.bal += amount
            print(f"Deposit done of amount:{amount}")
        else:
            print("Deposit amount to be +ve.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount to be +ve.")
        elif amount > self.bal:
            print("Low Balance")
        else:
            self.bal-= amount
            print(f"Withdrawn:{amount}")

    def display_account_details(self):
        print("Account Details")
        print(f"Account Number:{self.acc_number}")
        print(f"Account Holder:{self.name}")
        print(f"Current Balance:{self.bal}")

acc1 = Bank("123456789", "John",1000)
acc1.deposit(500)
acc1.withdraw(200)
acc1.display_account_details()