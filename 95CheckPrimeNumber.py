def prime(a):
    if a<=1:
        return 0

    else:
        for i in range(2,int((a)**(1/2))+1):
            if a%i==0:
                return 0
            else:
                return 1


number = int(input("Enter a number: "))
if prime(number):
    print("Prime number")
else:
    print("Not a prime number")

