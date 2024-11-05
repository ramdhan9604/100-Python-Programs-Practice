import math 

def check(a):
    root = math.isqrt(a)
    return root*root == a

a = int(input("Enter the number: "))

if check(a):
    print("Given number is Perfect Square Number.")
else:
    print("Given number is not Perfect Square Number.")