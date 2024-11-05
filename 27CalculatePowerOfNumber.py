def power_Number(num,power):
    return num**(power)

num = int(input("Enter the number: "))
power = float(input("Enter the power of the number: "))
result = power_Number(num,power)

print("The power of {num} is: ",result)