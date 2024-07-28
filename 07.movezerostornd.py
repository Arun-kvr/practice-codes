#brute force:
def movezerostoend(arr):
    n=len(arr)
    result=[]
    zero_count=0
    for i in range(n):
        if arr[i] !=0:
            result.append(arr[i])
        else:
            zero_count +=1
    result.extend([0]*zero_count)
    return(result)
#optimal:
def movezerostoend(arr):
    last_non_zero_found_at=0
    for i in range(len(arr)):
        if arr[i] !=0:
            arr[last_non_zero_found_at],arr[i]=arr[i],arr[last_non_zero_found_at]
            last_non_zero_found_at +=1
    return arr
arr=[int(x) for x in input().split()]
print(movezerostoend(arr))
# time complexity for both : O(n)