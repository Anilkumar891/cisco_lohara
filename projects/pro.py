class BankAccount:
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
            print("Account already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, account_name, initial_balance, address, phone_number, email)
            print("Account created successfully.")

    def display_account(self):
        account_number = input("Enter Account Number: ")

        if account_number in self.accounts:
            self.accounts[account_number].display_details()
        else:
            print("Account does not exist.")


def main():
    bank = Bank()

    while True:
        print("\nBank Account Management")
        print("1. Create Account")
        print("2. Display Account")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.display_account()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
