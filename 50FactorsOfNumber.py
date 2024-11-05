a = int(input("Enter the number: "))

factor = []

for i in range(1,a+1):
    if a%i==0:
        factor.append(i)

print("The factors of the given number are: ")
for i in factor:
    print(i)
