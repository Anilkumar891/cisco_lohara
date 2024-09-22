from BankAccount import BankAccount
import sqlite3
def connect():
    con = sqlite3.connect('notes_db.db')
    return con 


class Bank:
    
    def __init__(self):
        self.accounts = {}

    def noteTablesCreate():
        sql = """CREATE TABLE IF NOT EXISTS notes(
        id integer primary key AUTOINCREMENT,
        title varchar(255) not null,
        notes varchar(2000) not null
        )"""
        con = connect()
        con.execute(sql)
        con.close()
        print("Database is connected and in sync.")
class Note:
    def __init__(self,
        account_number='',
        account_name='',intial_balance='',address='',phone_number='',email=''):
        self.account_number = account_number
        self.account_name = account_name
        self.intial_balance=intial_balance
        self.address=address
        self.phone_number=phone_number
        self.email=email
    def __str__(self):
        return f'[{self.account_number},{self.account_name},{self.intial_balance,self.address,self.phone_number,self.email}]'
    def __repr__(self):
        return self.__str__()
    
    
    def create_account(self,note):
        sql = """INSERT INTO notes(account_number,account_name,intial_balance,address,phone_number,email)
        VALUES(?,?,?,?,?,?)"""
        params=(note.account_number,note.account_name,note.intial_balance,note.address,note.phone_number,note.email)
        

        if params.account_number in self.accounts:
            print("--------Account already exists.----------------")
           
        else:
            self.accounts[params.account_number] = BankAccount(params.account_number, params.account_name, params.initial_balance, params.address, params.phone_number, params.email)
            
            print("Account created successfully.")
            print("-------------------------------------Thank You------------------------------------------\n\n\n")
        con = connect()
        cur = con.cursor()
        cur.execute(sql,params)
        con.commit()
        con.close()
    
       
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
  