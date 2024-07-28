'''
# Brute force:
def left_rotate(arr):
    temp=arr[0]
    n=len(arr)
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
    return arr

arr=[int(x) for x in input().split()]
print(arr)
print(left_rotate(arr))
# time complexity : o(n)
'''
'''
arr=[1,2,3,4,5]
print(arr[1:])
print(arr[:1])
'''
# optimal :
def left_rotate(arr):
    return arr[1:]+arr[:1]
arr=[int(x) for x in input().split()]
print(left_rotate(arr))
#time complexity O(1)