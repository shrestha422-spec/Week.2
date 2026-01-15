class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
            
    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print(f"Withdrawal successful! New balance:{self.balance}")
        else:
            print("Insufficient balance or invalid amount.")