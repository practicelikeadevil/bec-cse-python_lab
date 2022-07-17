a=list()
n=int(input("enter how many words do you want:"))
for i in range(n):
    b=input("enter characters:")
    a.append(b)
print(a)
def list_slice(s,step):
    return [s[i::step] for i in range(step)]
c=int(input("enter slicnig point:"))
print("after slicing:")
print(list_slice(a,c))
