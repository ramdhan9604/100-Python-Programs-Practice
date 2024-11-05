a = int(input("Enter the lower point of range: "))
b = int(input("Enter the higher point of range: "))

li = []

for i in range(a,b+1):
    if i>1:
        prime = True       
        for j in range(2,i):
            if i%j==0:
                prime=False
                break
        if prime==True:
            li.append(i)
   


for i in li:
    print(i)

