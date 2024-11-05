a = int(input("Enter the number: "))


li = [i**2 for i in range(1,int(a**(0.5))+1)]

if a in li:
    print("Yes")
else:
    print("No")