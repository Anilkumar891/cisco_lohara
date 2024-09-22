from backend import c
from Bank import Bank
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
            bank.create_account()
        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)
        elif choice == '4':
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
