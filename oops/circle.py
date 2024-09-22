class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=3.14*self.radius*self.radius
        return area
    def para(self):
        parameter=2*3.14*self.radius
        return parameter
c1=circle(5)
print(c1.area())
print(c1.para())
print(c1.radius)