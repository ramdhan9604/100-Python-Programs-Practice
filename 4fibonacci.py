a = int(input("Enter the number: "))

def fib(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fib(a-1)+fib(a-2)


print("The fabonacci sequence is: ")
for i in range(a):
    print(fib(i))