a=input("write 'a' for ascending\nwrite 'd' for descending\ndo you want counting in ascending or descending:",)
if a=="a":
     i =int(input("upto which number should I write:",))
     x=1

     while x<=i:
      print(x)
      x+=1
elif a=="d":
   i =int(input("upto which number should I start:",))
   x=i
   while x>=1:
      print(x)
      x-=1     



