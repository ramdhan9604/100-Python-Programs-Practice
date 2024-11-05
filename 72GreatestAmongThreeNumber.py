def greatest(a,b,c):
    if a>b and a>c:
        return a
    
    elif b>c and b>a:
        return b

    else:
        return c 

a = 45
b = 57
c= 577

print("The greatest number is: ",greatest(a,b,c))