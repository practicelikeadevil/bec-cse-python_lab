a=input("enter string:")
b=a.split()[::-1]
l=[]
for i in b:
    l.append(i)
print(" ".join(l))
