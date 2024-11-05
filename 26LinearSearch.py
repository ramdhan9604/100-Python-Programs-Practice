def LinearSearch(arr,a):
    if a in arr:
        return 1
    else:
        return 0


a = int(input("Enter the size of the array: "))

print("Enter the element of the array: ")

arr = []

for i in range(a):
    b = int(input())
    arr.append(b)

num = int(input("Enter the element that you want to search in the given array: "))

if LinearSearch(arr,num)==1:
    print("Found")
else:
    print("Not Found")



        