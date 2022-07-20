from collections import Counter
l=[]
n=int(input("enter size of tuple:"))
for i in range(n):
    a=input("enter elements:")
    l.append(a)
t=tuple(l)
print("tuple is:",t)
rev=t[::-1]
print("after reversing the elements of tuple are:",rev)
