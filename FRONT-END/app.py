import json 
import requests
class banks:
    def __inif__(self,account_number,account_name,intial_balance):
        self.url='http://localhost:5000'
        self.account_number=account_number
        self.account_name=account_name
        self.intial_balance=intial_balance


    def __str__(self) -> str:
        return f'[account_number={self.account_number}],account_name={self.account_name},intial_balance={self.intial_balance}]'
    
    def __repr__(self) -> str:
        return self.__str__()
    

class banking:
    def __init__(self,account_number,account_name,intial_balance):
        self.account_number=account_number
        self.account_name=account_name
        self.intial_balance=intial_balance

    def __str__(self) -> str:
        return f'[Banking_NUMBER={self.account_number},Banking_Name={self.account_name},Intial_Account={self.intial_balance}]'

    def __repr__(self) -> str:
        return self.__str__()
        
            