def len_list(a):
    print(len(a))
b=int(input("How many inputs are there in your list:",))
a=[]
for i in range(b):
    temp=input(f"Enter the value of {i+1} ",)
    a.append(temp)
len_list(a)