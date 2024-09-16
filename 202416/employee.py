class anil:
    def __init__(self,name,address,code,salary):
        self.name=name
        self.address=address
        self.code=code
        self.salary=salary 
    def __str__(self): 
        return f'{self.name},{self.address},{self.code},{self.salary}'

anil2 =anil('anilkumar','2/24,anil ','puyth5678',20000)
print(anil2) 