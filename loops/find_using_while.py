no = int(input("How many element would be there in your tuple:",))
a=[]
i=0
while i<no:
   x = int(input("Enter your {} element: ".format(i + 1)))
   a.append(x)
   i+=1

i =int(input("which number do you want to find:",))
b=0
flag=True
while b<len(a):
    if i==a[b]:
        print("Yes,",i," is available")
        flag=False
        break
    b+=1         
if flag==True:
        print("No,",i," is not available")
           