a = input("Enter the number: ")



def aarmstrong_number(a):
    num=0
    n = len(a)
    for i in a:
        num = num+ int(i)**n
    if num==int(a):
        return 1
    else:
        return 0

if aarmstrong_number(a)==1:
    print("Given number is Aarmstrong Number.")
else:
    print("Given number is not Aarmstrong Number.")
