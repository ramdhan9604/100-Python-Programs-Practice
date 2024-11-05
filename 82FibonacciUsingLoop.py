def generate_fib(n):
    fib=[0,1]
    for i in range(2,n):
        next_n=fib[-1]+fib[-2]
        fib.append(next_n)
    return fib

terms=10

print("The fibonacci sequence is: ",generate_fib(terms))