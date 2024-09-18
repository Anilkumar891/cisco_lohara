""" def find_diff(first:int=1,second:int=0)->int:
    return first-second

print(find_diff(20,10))
print(find_diff(second=20,first=10))
print(find_diff(second=10))
print(find_diff())


def change_name(names,index,name):
    names[index]=name


names=['rahul','modi'] 
print(names)
change_name(names,1,'kk')
print(names) 
change_name(names,0,'modiji')

print(names)  


def find_sum(first,second,*others):
    s=first+second
    if(len(others)>0):
        for num in others:
            s+=num
    return s

print(find_sum(10,20))
print(find_sum(10,20,30))
print(find_sum(10,20,30,40,50))      """ 
""" 

def find_sum(first,second,**others):
    s=first+second
    if(len(others)>0):
        for key in others:
            s+=others[key]
    #print(type(others))        
    return s

print(find_sum(first=10,second=20))
print(find_sum(first=10,second=20,third=30))
print(find_sum(first=10,second=20,third=30,forth=40))
 """

def fact(N):
    if N<=1:
        return 1
    return N * fact(N-1)
    

print(fact(5)) 


import math
def is_prime(N):
    N_sqrt=int(math.sqrt(N))
    for i in range(2,N_sqrt+1):
        if N%i==0:
            return False
    return True

print(is_prime(5))
print(is_prime(51))    


    



