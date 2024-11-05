a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

s = (a+b+c)/2.0


import math 

area = math.sqrt(s*(s-a)*(s-b)*(s-c)) 

print("The area of the triangle is: ",area)
