def n_sum(n):
    if n==1:
        return n
    else:
        return n+n_sum(n-1)


a = int(input("Enter the number of terms: "))
print(n_sum(a))