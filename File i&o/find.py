word="learning"
with open("D:\programming languages\python\complete project\small project\File i&o\practice.txt","r") as f:
    data=f.read()
    if word in data:
        print("found")
    else:
        print("not found")    
