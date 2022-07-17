def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter a number:"))
if n<0:
    print("factorial is not possible for negative numbers")
elif n==0:
    print("factorial is 1")
else:
    print("factorial is:",factorial(n))
