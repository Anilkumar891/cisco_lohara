class Account:
    def __init__(self,number,name,initial_amount=1000):
        self.__number=number
        self.__name=name
        self.__balance=initial_amount
    def __repr__(self):
        return f'[number={self.__number},name={self.__name},balance={self.__balance}]'

    def __str__(self):
        return self.__repr__()
    
    def deposit(self,amount):
        self.__balance +=amount

    def withdraw(self,amount):
        if amount>self.__balance:
            print("no enough amount")
            return
            
        self.__balance -=amount        

rohit_ac=Account(name='rohit',number='123456546512',initial_amount=3000)
print(rohit_ac)
rohit_ac.deposit(200000)
print(rohit_ac)
rohit_ac.deposit(10000)
print(rohit_ac)
rohit_ac.withdraw(5000000)
print(rohit_ac)
print(rohit_ac.__dict__)
""" print(rohit_ac.__balance) """