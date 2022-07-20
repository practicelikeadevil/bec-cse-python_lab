from collections import Counter
data=input("enter data:")
split_data=data.split()
Counter=Counter(split_data)
n=int(input("enter how many numbers do you want:"))
most_occur=Counter.most_common(n)
print(most_occur)
