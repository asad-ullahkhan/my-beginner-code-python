with open("D:\programming languages\python\complete project\small project\File i&o\practice.txt","r") as f:
    data=f.read()
new_data=data.replace("java","python")    
with open("D:\programming languages\python\complete project\small project\File i&o\practice.txt","w") as f:
    f.write(new_data)
