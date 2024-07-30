#brute force:
def left_rotatebyd(arr,d):
    n=len(arr)
    for _ in range(d):
        temp=arr[0]
        for i in range(n-1):
            arr[i]=arr[i+1]
        arr[n-1]=temp
    return(arr)

# Time complexity : O(d*n)


#optimal:
def left_rotatebyd(arr,d):
    n=len(arr)-1
    return arr[d:]+arr[:d]

arr=[int(x) for x in input().split()]
d=int(input("Enter d:"))
print(left_rotatebyd(arr,d))
#time complexity :  O(1)