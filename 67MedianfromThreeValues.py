li =[]

print("Enter three numbers: ")
for i in range(3):
    a = float(input())
    li.append(a)

li1 = sorted(li)

print("The median is : ",li1[1])
