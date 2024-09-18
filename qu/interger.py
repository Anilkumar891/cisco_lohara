n=input("enter the number:").split()
s=tuple(n)
print(s)
s2=set(n)
print(s2)
s3=frozenset(n)
print(s3)
names_dict={n:len(n) for n in names_fset}
print(names_dict)

