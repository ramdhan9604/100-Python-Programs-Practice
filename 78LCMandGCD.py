# def LCM(a,b):
#     if a>b:
#         lar = a
#     else:
#         lar = b
    
#     while True:
#         if lar%a==0 and lar%b==0:
#             lcm = lar
#             break
#         lar=lar+1
#     return lcm

def LCM(a,b):
    lcm = (a*b)/(GCD(a,b))
    return lcm

def GCD(a,b):
    while b:
        a,b= b,a%b
    return a

a = 34
b = 111

print("The GCD is: ",GCD(a,b))
print("The LCM is: ",LCM(a,b))