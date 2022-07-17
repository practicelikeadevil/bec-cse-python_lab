list1=list()
list2=list()
string1="Hello everyone\ngood morning to one and all\nToday is the first day of our demo session"
string2="Guys i think all are ready\nso without any delay \nlet's get started"
print(string1)
print('\n',string2,'\n')
list1=string1.split('\n')
list2=string2.split('\n')
for i in range(len(list1)):
    print(list1[i]+'\n'+list2[i])
