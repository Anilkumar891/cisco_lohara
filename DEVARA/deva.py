import datetime
import logging
import os
import sqlite3
from celery import Celery
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from paramiko import SSHClient

from smtplib import SMTP
from bs4 import BeautifulSoup
import redis

# Configure logging
logging.basicConfig(filename='bank_account_management.log', level=logging.INFO)

# Create Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank_account_management.db'
db = SQLAlchemy(app)

# Create Celery app
celery = Celery('bank_account_management', broker='redis://localhost:6379/0')

# Define database models
class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), unique=True)
    account_name = db.Column(db.String(50))
    balance = db.Column(db.Float)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('(link unavailable)'))
    transaction_date = db.Column(db.DateTime)
    transaction_type = db.Column(db.String(10))
    amount = db.Column(db.Float)

# Define tasks
@celery.task
def update_account_balance(account_id, amount):
    account = Account.query.get(account_id)
    account.balance += amount
    db.session.commit()

@celery.task
def send_email_alert(account_id, transaction_type, amount):
    account = Account.query.get(account_id)
    # Send email using SMTP
    smtp = SMTP('(link unavailable)', 587)
    smtp.starttls()
    smtp.login('dubaanilkumar99@gmail.com', 'your_password')
    smtp.sendmail('dubaanilkumar99@gmail.com', account.account_name + '@email.com', 
                  'Subject: Transaction Alert\n\n' + 
                  'Account Number: ' + account.account_number + '\n' + 
                  'Transaction Type: ' + transaction_type + '\n' + 
                  'Amount: ' + str(amount))
    smtp.quit()

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    account_number = request.form['account_number']
    account_name = request.form['account_name']
    balance = float(request.form['balance'])
    account = Account(account_number=account_number, account_name=account_name, balance=balance)
    db.session.add(account)
    db.session.commit()
    return 'Account created successfully!'

@app.route('/deposit', methods=['POST'])
def deposit():
    account_id = int(request.form['account_id'])
    amount = float(request.form['amount'])
    update_account_balance.apply_async(args=[account_id, amount])
    send_email_alert.apply_async(args=[account_id, 'Deposit', amount])
    return 'Deposit successful!'

@app.route('/withdraw', methods=['POST'])
def withdraw():
    account_id = int(request.form['account_id'])
    amount = float(request.form['amount'])
    update_account_balance.apply_async(args=[account_id, -amount])
    send_email_alert.apply_async(args=[account_id, 'Withdrawal', amount])
    return 'Withdrawal successful!'

# Run app
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)