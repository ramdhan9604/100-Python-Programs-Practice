a = int(input("Enter the number: "))

def prime_n(a):
    # for i in range(2,a):
    for i in range(2, int(a ** 0.5) + 1):
        if a%i==0:
            return 0
    else:
        return 1

if(prime_n(a)==0):
    print("Not Prime")
else:
    print("Prime")