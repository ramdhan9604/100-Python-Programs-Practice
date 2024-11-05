def binary_Search(arr,x):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>x:
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
        else:
            return mid 
    return -1

arr = [1,2,3,4,5,6,7,8]

r = binary_Search(arr,5)

if r!=-1:
    print(f"The element found at index {r}")
else:
    print("Element is not found.")