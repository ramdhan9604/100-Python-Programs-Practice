base = int(input("Enter the base :"))
exponent = int(input("Enter the exponent: "))

result=1
for _ in range(exponent):
    result=result*base


print("Result is:",result)