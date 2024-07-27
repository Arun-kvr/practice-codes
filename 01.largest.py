#brute force:
def largest(arr):
    arr.sort()
    n=len(arr)
    return arr[n-1]
arr=[int(x) for x in input().split()]
print(largest(arr))
#tc=log(n)+n=O(nlogn)

#optimal:
def largest(arr):
    large=arr[0]
    n=len(arr)
    for i in range(0,n-1):
        if arr[i]>large:
            large=arr[i]
    return large
arr=[int(x) for x in input().split()]
print(largest(arr))
#tc=O(n)