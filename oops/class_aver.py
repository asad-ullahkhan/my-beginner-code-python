class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        sum=0
        for val in self.marks:
            sum+=val

        print(f"the average is {sum/3}")
s1=student("asad",[98,97,96])
print(s1.average())