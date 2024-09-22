from c import create_database,add_account,check_balance,deposit,withdraw,transfer_file,send_email_alert,process_transactions,run_concurrent_tasks

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
  

class Bank:
    
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input("Enter Account Number: ")
        account_name = input("Enter Account Name: ")
        initial_balance = float(input("Enter Initial Balance: "))
        address = input("Enter Address: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")


        if account_number in self.accounts:
            print("--------Account already exists.----------------")
           
        else:
            self.accounts[account_number] = BankAccount(account_number, account_name, initial_balance, address, phone_number, email)
            
            print("Account created successfully.")
            print("-------------------------------------Thank You------------------------------------------\n\n\n")

    
       
    def display_account(self):
        account_number = input("Enter Account Number: ")

        if account_number in self.accounts:
            self.accounts[account_number].display_details()
        else:
            print("Account does not exist.")  
    
    def find_account(self, account_number):
        return self.accounts.get(account_number, None)

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")
    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} has been closed.")
        else:
            print("Account not found.")

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        else:
            print("\nAll Accounts:")
            for account in self.accounts.values():
                account.display()        


def main():
    bank = Bank()

    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Account Details")
        print("5. Close Account")
        print("6. View All Accounts")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            id=int(input("enter the number"))
            account_number = input("Enter Account Number: ")
            account_name = input("Enter Account Name: ")
            initial_balance = float(input("Enter Initial Balance: "))
            address = input("Enter Address: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            create_database()
            add_account(account_name,initial_balance)
            bank.create_account()
        elif choice == '2':
            check_balance(id)
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)
        elif choice == '3':
           
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            amount2 = float(input("Enter deposit amount: "))
            process_transactions(id,amount,amount2)
            check_balance(id)
            bank.withdraw(account_number, amount)
        elif choice == '4':
            run_concurrent_tasks()
            bank.display_account()
        elif choice == '5':
            account_number = input("Enter account number: ")
            bank.close_account(account_number)
        elif choice == '6':
            bank.display_all_accounts()
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")



main()

