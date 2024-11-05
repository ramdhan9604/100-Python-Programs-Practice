def merge_sort(arr):
    n = len(arr)
    if n>1:
        mid = n//2
        left_half=arr[:mid]
        right_half=arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i=j=k=0

        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                arr[k]=left_half[i]
                i=i+1
            else:
                arr[k]=right_half[j]
                j=j+1
            
            k=k+1

        while i<len(left_half):
            arr[k]=left_half[i]
            i=i+1
            k=k+1
        
        while j<len(right_half):
            arr[k]=right_half[j]
            j=j+1
            k=k+1
    
    return arr
        

arr = [1,2,3,4,590,87,65,32]

sorted_arr=merge_sort(arr)

print("After merge sort: ",sorted_arr)
        

