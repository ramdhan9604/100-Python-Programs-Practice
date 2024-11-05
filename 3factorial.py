a = int(input("Enter the number: "))

def factorial(a):
    if a==0:
        return 1
    else:
        return a*factorial(a-1)

print("Factorial of the given number is: ",factorial(a))
