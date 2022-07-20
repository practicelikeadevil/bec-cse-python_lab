from collections import Counter
l=[]
n=int(input("enter size of tuple:"))
for i in range(n):
    a=input("enter elements:")
    l.append(a)
t=tuple(l)
c=Counter(t)
print("the tuple is:",t)
t1=tuple(dict.fromkeys(t))
c1=Counter(t1)
print("the repeated items in a tuple are:",tuple(dict.fromkeys(c-c1)))
