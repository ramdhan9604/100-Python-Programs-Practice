def Binary_Search(arr,low,high,element):
    if high>=low:
        mid = (low+high)//2
        if arr[mid]==element:
            return mid
        elif arr[mid]>element:
            return Binary_Search(arr,low,mid-1,element)
        else:
            return Binary_Search(arr,mid+1,high,element)

    return -1

# arr,mid+1,high,element
# arr,low,mid-1,element

li =[1,2,3,4,5,6,7]

result = Binary_Search(li,0,len(li)-1,7)

if result!=-1:
    print(f"Element found at index {result}")
else:
    print("Element not found.")