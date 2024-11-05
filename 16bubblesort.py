def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

a = int(input("Enter the size of the array: "))

print("Enter the element of the array: ")

arr = []

for i in range(a):
    a =int(input())
    arr.append(a)
    
print("Sorted elements:")
for i in bubblesort(arr):
    print(i)
