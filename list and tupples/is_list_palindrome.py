list1=[]
list1.append(input("Enter your first number: ",))
list1.append(input("Enter your second number: ",))
list1.append(input("Enter your third number: ",))
list1.append(input("Enter your forth number: ",))
list1.append(input("Enter your fifth number: ",))
lista=list1.copy()
list1.reverse()
if list1==lista :
    print("Yes list1 is a palindrome")
else:
    print("No list1 is not a palindrome")    