#brute force:
def secondlargest(arr):
    arr.sort()
    n=len(arr)
    if arr[n-1]>arr[n-2]:
        return arr[n-2]
    else:
        while arr[n-1] == arr[n-2]:
            n=n-1
        return arr[n-2]
    
arr=[int(x) for x in input().split()]
print(secondlargest(arr))
#time complexity nlog(n)+n

#optimal:
def second_largest_element(arr):
    first_largest_element=arr[0]
    second_largest_element=-1
    n=len(arr)-1
    for i in range(n):
        if arr[i]>first_largest_element:
            second_largest_element=first_largest_element
            first_largest_element=arr[i]
        else:
            second_largest_element=arr[i]
        i=i+1
    return(second_largest_element)

arr=[int(x) for x in input().split()]
print(second_largest_element(arr))

#time complexity: O(n)