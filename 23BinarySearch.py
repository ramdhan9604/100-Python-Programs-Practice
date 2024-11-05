def BinarySearch(arr,x):
    a = len(arr)
    low = 0
    high = a-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>x:
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
        else:
            return mid
    
    return -1

arr = [1,2,3,40,50,60,70]

a = int(input("Enter the element that you want to search: "))

b=BinarySearch(arr,a)
if b!=-1:
    print(f"The element found at index 6{b}")
else:
    print("Element not found.")



    