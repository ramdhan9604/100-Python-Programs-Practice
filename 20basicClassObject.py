class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width


l = float(input("Enter the length of the rectangle: "))
w = float(input("Enter the width of the rectangle: "))

a= rectangle(l,w)
print("The area of the rectangle is: ",a.area())