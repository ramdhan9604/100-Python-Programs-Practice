def fibonacciSeries(n):
    a = 0
    b = 1
    for i in range(n):
        print(a," ")
        a,b=b,a+b

num = int(input("Enter the number of terms of Series: "))

print("The fibonacci Series is: ")
fibonacciSeries(num)


