a=input("enter  any string:")
total=0
vowels=0
for i in a:
    total+=1
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels+=1
print("number of vowels:")
print(vowels)
print("percentage of vowels:")
print(vowels*100//total)
        
