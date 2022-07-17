list1=list()
string="hello everyone\nwelcome to python programming\ngood to see you all"
list1=string.split('\n')
n=int(input("enter line no:"))
for i in range(len(list1)):
    if n==i:
        print(list1[i-1])
