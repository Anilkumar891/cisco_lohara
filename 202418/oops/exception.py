class Myexception(ZeroDivisionError):
    pass
def find_quotient(d,n):
    if n==0:
        raise ZeroDivisionError()
    return d/n

try:
    number=int(input("enter he number:"))
    result=find_quotient(10,number)
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print('divided error') 

except Myexception:
    print('end of the era')    
else:
    print(result)
finally:
    print("cleamih")
print("end the program")