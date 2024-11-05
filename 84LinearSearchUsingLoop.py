def Linear_search(arr,x):
    n = len(arr)
    for i in range(n):
        if arr[i]==x:
            return i
    return -1

arr = [4,2,1,7,5]
x=7

f = Linear_search(arr,x)

if f!=-1:
    print(f"Element found at index {f}")
else:
    print("Element is not found.")