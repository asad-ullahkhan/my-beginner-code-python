def line_find(x):
    with open(r"D:\programming languages\python\complete project\small project\File i&o\practice.txt","r") as f:
        lines=f.readlines()
        for i,line in enumerate(lines):
            if x in line:
                print(f"{x} is in line {i+1}")
                break
        else:
                print(f"{x} is not found in any line")    

x=input("which word do you want to find:")
line_find(x)