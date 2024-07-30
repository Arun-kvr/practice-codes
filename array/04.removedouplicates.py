# Brute force:
def remove_douplicates(arr):
    new_arr=[]
    for i in range(len(arr)):
        is_douplicate=False
        for j in range(len(new_arr)):
            if arr[i]==new_arr[j]:
                is_douplicate=True
                break
        if not is_douplicate:
            new_arr.append(arr[i])
    return new_arr

arr=[int(x) for x in input().split()]
print(remove_douplicates(arr))

# time complexity = O(n**2)

# using set:
def remove_douplicates(arr):
    return list(set(arr))

arr=[int(x) for x in input().split()]
print(remove_douplicates(arr))

# time complexity : o(n**2) 

# optimal solution:

def remove_douplicates(arr):
    seen=set()
    result=[]
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

arr=[int(x) for x in input().split()]
print(remove_douplicates(arr))

# time complexity : O(n)