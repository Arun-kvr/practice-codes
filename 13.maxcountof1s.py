# brute force :
def maxcount(arr):
    maxcount=0
    for i in range(len(arr)):
        count=0
        for j in range(i,len(arr)):
            if arr[j]==1:
                count+=1
            else:
                break
        maxcount=max(count,maxcount)
    return(maxcount)
arr=[int(x) for x in input("enter arr").split()]
print(maxcount(arr))
#timecomplexity:O(n^2)

# optimal solution :
def maxcount(arr):
    maxcount=0
    count=0
    for i in range(len(arr)):
        if arr[i]==1:
            count+=1
            maxcount=max(count,maxcount)
        else:
            count=0
    return maxcount
arr=[int(x) for x in input("enter arr").split()]
print(maxcount(arr))
#timecomplexity:O(n)
