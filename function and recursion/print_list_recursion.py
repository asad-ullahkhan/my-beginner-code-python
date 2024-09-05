def print_list(a,i):
    if i==len(a):
        return
    else:
        print(a[i],end=" ")
        print_list(a,i+1)
b=int(input("How many inputs are there in your list:",))
a=[]
for i in range(b):
    temp=input(f"Enter the value of {i+1} ",)
    a.append(temp)
print_list(a,0)  