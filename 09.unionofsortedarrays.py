# brute force:
def union_of_sorted_arrays(arr1,arr2):
    target=[]
    for num in arr1:
        if num not in target:
            target.append(num)
    for num in arr2:
        if num not in target:
            target.append(num)
    return sorted(target)
arr1=[int(x) for x in input().split()]
arr2=[int(x) for x in input().split()]
print(union_of_sorted_arrays(arr1,arr2))
# time complexity O(m+n+nlogn)

# optimal solution :
def union(arr1,arr2):
    i,j=0,0
    union=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j+=1
        else:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
            j+=1
    while i<len(arr1):
        if not union or union[-1]!=arr1[i]:
            union.append(arr1[i])
        i+=1
    while j<len(arr2):
        if not union or union[-1]!=arr2[j]:
            union.append(arr2[j])
        j+=1
    return union

arr1=[int(x) for x in input().split()]
arr2=[int(x) for x in input().split()]
print(union(arr1,arr2))
# time complexity : O(m+n)

# using set :
def union(arr1,arr2):
    set1=set(arr1)
    set2=set(arr2)
    union_set=set1.union(set2)
    union_list=list(union_set)
    return union_list
arr1=[int(x) for x in input().split()]
arr2=[int(x) for x in input().split()]
print(union(arr1,arr2))
#time complexity:o(m+n)


