# brute force :
def findmissingelement(arr):
    n=len(arr)+1
    for i in range(1,n+1):
        if i not in arr:
            return i
arr=[1,2,3,4,5]
print(findmissingelement(arr))
#time complexity : O(n^2)

# optimal solution :
def findmissingelement(arr):
    n=len(arr)+1
    total_sum=n*(n+1)//2
    arr_sum=sum(arr)
    return total_sum-arr_sum
arr=[int(x) for x in input().split()]
print(findmissingelement(arr))
#timecomplexity=O(n)
