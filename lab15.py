def python():
    a=list()
    n=int(input("enter size of the list:"))
    for i in range(n):
        b=int(input("enter number:"))
        a.append(b)
    print("the list is:",a)
    max=a[0]
    min=a[0]
    for i in a:
        if i>max:
            max=i
        if i<min:
            min=i
    print("maximum element is:",max)
    print("minimum element is:",min)
python()
