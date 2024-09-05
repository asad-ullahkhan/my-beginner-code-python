def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
n=int(input("which number factorial do you want:",))
print(fact(n))