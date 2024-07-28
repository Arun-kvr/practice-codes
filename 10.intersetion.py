# brute force :
def intersection(arr1,arr2):
    intersection=[]
    for num1 in arr1:
        for num2 in arr2:
            if num1==num2 and num1 not in intersection:  
                intersection.append(num1)
    return intersection

arr1=[int(x) for x in input("Enter first array").split()]
arr2=[int(x) for x in input("Enter second array").split()]
print(intersection(arr1,arr2))
# time complexity : O(n^2)

# using set :
def intersection(arr1,arr2):
    return list(set(arr1)&set(arr2))

arr1=[int(x) for x in input("Enter first array").split()]
arr2=[int(x) for x in input("Enter second array").split()]
print(intersection(arr1,arr2))
# time complexity : O(m+n)