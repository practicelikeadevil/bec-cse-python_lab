from collections import Counter
l=[]
n=int(input("enter size of tuple:"))
for i in range(n):
    a=input("enter elements:")
    l.append(a)
print("list is:",l)
t=tuple(dict.fromkeys(l))
print("tuple without duplicates:",t)
