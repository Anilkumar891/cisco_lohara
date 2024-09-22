from flask import Flask,jsonify,request
from db import bank,bank_create,__init__,add_account,check_balance,deposit,withdraw

bank_create()
app=Flask(__name__)

def __init__(self):
        self.accounts = {}

@app.route('/bank',methods=['POST'])
def add_account(self,account_number,account_name,intial_balance):

    if account_number in self.accounts:
        print("account is alredy exited")
    else:
         self.accounts[account_number]=bank[account_number,account_name,intial_balance]
         print("account added succesfully")

@app.route('/bank/<account_number>',methods=['GET'])
def check_balance(self):
      return self.intial_balance

@app.route('/bank/<account_number>',methods=['POST'])
def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

@app.route('/bank/<account_number>',methods=['GET'])
def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")