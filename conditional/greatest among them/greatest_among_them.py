num1=int(input("Enter your first number: ",))
num2=int(input("Enter your second number: ",))
num3=int(input("Enter your third number: ",))
if num1>num2:
    if num1>num3:
        print(num1,"is the greates among them")
    elif num1<num3:
        print(num3,"is the greates among them")
elif num1<num2:
    if num2>num3:
        print(num2,"is the greates among them")
    elif num2<num3:
        print(num3,"is the greates among them")
    