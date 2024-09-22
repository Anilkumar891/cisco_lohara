class BankAccount:

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nAmount {amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount should be positive.")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"\nAmount {amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def display(self):
        print("\nAccount Information:")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_name}")
        print(f"Account Balance: {self.balance}") 

    def __init__(self, account_number, account_name, balance=0, address="", phone_number="", email=""):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Name: {self.account_name}")
        print(f"Balance: {self.balance}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email: {self.email}")     
  