def factorial(a):
    if a<=0:
        return 1
    else:
        return a*factorial(a-1)

a = 6

print(f"The factorial of {a} is:",factorial(a))