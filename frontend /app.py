import json
from backend import c


def main():
    

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
            account_number = input("Enter Account Number: ")
            account_name = input("Enter Account Name: ")
            initial_balance = float(input("Enter Initial Balance: "))
            address = input("Enter Address: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            notes_dict={'account_number':account_number,'account_name':account_name,'intial_balance':initial_balance,
                         'address':address,'phone_number':phone_number,'email':email}
            note_json_str=json.dumps(notes_dict)
            note=bank.create_account(note_json_str)

            
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