import sqlite3
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import json

# SQLite3 database connection
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

# Web scraping function
def scrape_exchange_rate():
    url = '(link unavailable)'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    exchange_rate = soup.find('p', {'class': 'rate'}).text.strip()
    return exchange_rate

# Email alert function
def send_email_alert(subject, body, to_email):
    from_email = 'your_email@gmail.com'
    password = 'your_password'
    server = smtplib.SMTP('(link unavailable)', 587)
    server.starttls()
    server.login(from_email, password)
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

# Bank management class
class Bank:
    def __init__(self):
        self.conn = conn
        self.cursor = cursor

    def create_customer(self, name, email, phone, address):
        self.cursor.execute('''
            INSERT INTO customers (name, email, phone, address)
            VALUES (?, ?, ?, ?)
        ''', (name, email, phone, address))
        self.conn.commit()

    def create_account(self, customer_id, account_type, balance):
        self.cursor.execute('''
            INSERT INTO accounts (customer_id, account_type, balance)
            VALUES (?, ?, ?)
        ''', (customer_id, account_type, balance))
        self.conn.commit()

    def deposit(self, account_id, amount):
        self.cursor.execute('SELECT balance FROM accounts WHERE id=?', (account_id,))
        balance = self.cursor.fetchone()[0]
        balance += amount
        self.cursor.execute('UPDATE accounts SET balance=? WHERE id=?', (balance, account_id))
        self.cursor.execute('''
            INSERT INTO transactions (account_id, transaction_type, amount, timestamp)
            VALUES (?, 'deposit', ?, datetime('now'))
        ''', (account_id, amount))
        self.conn.commit()
        send_email_alert('Deposit Alert', f'Deposited ${amount} into account {account_id}', 'customer_email@example.com')

    def withdraw(self, account_id, amount):
        self.cursor.execute('SELECT balance FROM accounts WHERE id=?', (account_id,))
        balance = self.cursor.fetchone()[0]
        if amount > balance:
            print("Insufficient funds")
            return
        balance -= amount
        self.cursor.execute('UPDATE accounts SET balance=? WHERE id=?', (balance, account_id))
        self.cursor.execute('''
            INSERT INTO transactions (account_id, transaction_type, amount, timestamp)
            VALUES (?, 'withdrawal', ?, datetime('now'))
        ''', (account_id, amount))
        self.conn.commit()
        send_email_alert('Withdrawal Alert', f'Withdrew ${amount} from account {account_id}', 'customer_email@example.com')

    def check_balance(self, account_id):
        self.cursor.execute('SELECT balance FROM accounts WHERE id=?', (account_id,))
        balance = self.cursor.fetchone()[0]
        print(f"Balance: {balance}")

# Postman API integration
import requests

def postman_api_request(endpoint, data):
    url = f'(link unavailable)'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Main function
def main():
    bank = Bank()

    while True:
        print("\nBank Management System\n")
        print("1. Create Customer")
        print("2. Create Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
main()

