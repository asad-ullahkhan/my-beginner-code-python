no = int(input("How many element would be there in your tuple:",))
a=[]
i=0
while i<no:
   x = int(input("Enter your {} element: ".format(i + 1)))
   a.append(x)
   i+=1

i =int(input("which number do you want to find:",))
flag=True
for el in a:
   if el ==i:
      print("yes,",i,"is availble")
      flag=False
else :
   print("No,",i,"is not available")      