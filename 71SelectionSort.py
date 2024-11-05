# Selection Sort

def Selection_Sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j

        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    
    return arr 


arr = [1,67.48,90,23,13]

print("After Selection Sort the array: ",Selection_Sort(arr))