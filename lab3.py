from collections import Counter
data=input("enter data:")
split_data=data.split()
Counter=Counter(split_data)
n=int(input("how many most occurred words do you need:"))
most_occur=Counter.most_common(n)
print("most occurred words:",most_occur)
