def print_list(a):
    for i in range(len(a)):
        print(a[i],end="")
b=int(input("How many inputs are there in your list:",))
a=[]
for i in range(b):
    temp=input(f"Enter the value of {i+1} ",)
    a.append(temp)
print_list(a)  