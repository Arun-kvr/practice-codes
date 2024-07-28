# brute force :
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[int(x) for x in input().split()]
target=int(input("enter target :"))
print(linear_search(arr,target))
# time complexity = O(n)
# optimal :
def linear_search(arr,target):
    try:
        return arr.index(target)
    except ValueError:
        return -1
arr=[int(x) for x in input().split()]
target=int(input("enter the target :"))
print(linear_search(arr,target))
# time complexity : O(n)