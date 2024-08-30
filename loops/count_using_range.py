a=input("write 'a' for ascending\nwrite 'd' for descending\ndo you want counting in ascending or descending:",)
if a=="a":
     i =int(input("upto which number should I write:",))
     for el in range(i):
         print(el)

elif a=="d":
   i =int(input("upto which number should I start:",))
   for el in range(i,0,-1):
       print(el) 
