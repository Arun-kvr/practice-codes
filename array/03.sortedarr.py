def sorted_arr(arr):
    n=len(arr)-1
    for i in range(0,n):
        if arr[i]>arr[i+1]:
            return "array is not sorted"
    return "array is sorted"

arr=[int(x) for x in input().split()]
print(sorted_arr(arr))

# time complexity : O(n)