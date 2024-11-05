# li = ['A','H','B','E']

l = []

n = int(input("Enter the number of strings in list: "))
print("Enter the element of the list as string:")

for i in range(n):
    b = input()
    l.append(b)



li = sorted(l)

# for i in b:
#     print(i)

print("Sorted List of string is:",li)