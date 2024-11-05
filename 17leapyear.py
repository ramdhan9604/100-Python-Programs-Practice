a = int(input("Enter the year: "))


def leap_year(a):
    if a%100!=0 and a%4==0:
        return 1
    elif a%100==0 and a%400==0:
        return 1
    else:
        return 0

if leap_year(a)==1:
    print("Leap Year")
else:
    print("Not Leap Year")


