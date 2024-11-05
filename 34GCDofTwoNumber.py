a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# def GCD(a,b):
#     num = 1
#     if a>b:
#         small=a
#     else:
#         small=b
    
#     for i in range(1,small+1):
#             if a%i==0 and b%i==0:
#                 a,b=a/i,b/i
#                 num = num*i
    
#     return num

# print("GCD is: ",GCD(a,b))

# print(15%30)

def GCD(x, y):
    while y:
        x, y = y, x % y
    return x
print("GCD is: ",GCD(a,b))