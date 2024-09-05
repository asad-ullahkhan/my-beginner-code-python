def fact(n):
    current=1
    for i in range(n,0,-1):
        current*=i
    print(current)
n=int(input("which number factorial do you want:",))
fact(n)