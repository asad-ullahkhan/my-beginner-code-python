class employee:
    def __init__(self,role,dep,salr):
        self.role=role
        self.dep=dep
        self.salr=salr
    def showdetails(self):
        print("role=",self.role)
        print("department=",self.dep)
        print("salery=",self.salr)
class engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","IIT",55000)
e1=employee("accountant","Finance",45000)
en1=engineer("ASAD",19)
e1.showdetails()
en1.showdetails()
