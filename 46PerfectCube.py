num = int(input("Enter the number: "))

a = round(num**(1/3))

if a**3==num:
    print("The given number is perfect cube.")
else:
    print("The given number is not perfect cube.")