num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)

print("GCD of given numbers is: ",GCD(num1,num2))
