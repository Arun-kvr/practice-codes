def unionandintersection(arr1,arr2):
    list1= list(set(arr1).union(set(arr2)))
    list2= list(set(arr2)&set(arr2))
    return list1,list2
arr1=[int(x) for x in input("enter arr1:").split()]
arr2=[int(x) for x in input("enter arr2:").split()]
print(unionandintersection(arr1,arr2))
# time complexity : O(m+n)
    