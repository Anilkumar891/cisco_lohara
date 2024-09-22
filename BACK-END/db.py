import sqlite3
import json

def connect():
    con = sqlite3.connect('bank_db')
    return con
# Create a 'bank_account' table if it doesn't exist already
def bank_create():
    sql="""CREATE TABLE IF NOT EXISTS bank(account_number integer primary key ,account_name varchar(255)not null,intial_balance integer not null)"""
    con=connect()
    con.execute(sql)
    con.close()

class bank:
    
    def __init__(self, account_number=None,account_name='',intial_balance=0):
        self.account_number =account_number
        self.account_name = account_name
        self.intial_balance= intial_balance
    # CRUD operations for airplanes
    #     
    def add_account(account_name):
        sql="""INSERT INTO bank(account_number,account_name,intial_balance) VALUES(?,?,?)"""
        params=(bank.account_number,bank.account_name,bank.intial_balance)
        con=connect()
        cur=con.cursor()
        cur.execute(sql,params)
        account_number=cur.lastrowid
        con.commit()
        con.close()
        return account_number
    def check_balance(account_number):
        sql=""""SELECT account_number,account_name,intial_balance FROM bank"""
        con=connect()
        cur=con.cursor()
        response=cur.execute(sql)
        result=response.fetchall()[0]
        con.close()
        return result
    def deposit(account_number,amount):
       
       #sql="""UPDATE bank SET intial_balance=intial_balance+ ? WHERE account_number=?"""
        #params=(account_number,account_name,intial_balance)
        """ con=connect()
        cur=con.cursor()
        cur.execute(sql,params)
        con.commit()
        con.close() """
        import sqlite3  # Import only needed for this function
        conn = sqlite3.connect('bank_db')  # Connect to the database
        cursor = conn.cursor()             # Create a cursor object
    
    # Update the balance by adding the deposit amount
        cursor.execute('UPDATE bank_account SET balance = balance + ? WHERE account_id = ?', 
                   (amount, account_number))
    
        conn.commit()  # Commit the transaction
        conn.close()   # Close the connection

    def withdraw(account_number, amount):
        import sqlite3  # Import only needed for this function
        conn = sqlite3.connect('bank_db')  # Connect to the database
        cursor = conn.cursor()             # Create a cursor object
    
    # Check current balance before withdrawing
        cursor.execute('SELECT balance FROM bank_account WHERE account_id = ?', (account_number,))
        balance = cursor.fetchone()[0]     # Get the current balance
    
        if balance >= amount:
        # If there are enough funds, update the balance by subtracting the withdrawal amount
            cursor.execute('UPDATE bank_account SET balance = balance - ? WHERE account_id = ?', 
                       (amount, account_number))
            conn.commit()  # Commit the transaction
        else:
            print("Insufficient funds")    # If not enough balance, display a message
    
            conn.close()  # Close the connection    

    






   
    






   





      
      