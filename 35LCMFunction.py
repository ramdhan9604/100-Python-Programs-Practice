def Leap(a):
    if a%100==0:
        if a%400==0:
            return 1
        else:
            return 0
    else:
        if a%4==0:
            return 1
        else:
            return 0

year = int(input("Enter the year: "))

if Leap(year):
    print("Leap Year")
else:
    print("Not Leap Year")
