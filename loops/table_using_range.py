b = int(input("enter the multiplicant: ",))
a = int(input("enter the multiplicator: ",))
i=1
for el in range(b,(b*a)+1,b):
    print(b,"*",i,"=",el)
    i+=1