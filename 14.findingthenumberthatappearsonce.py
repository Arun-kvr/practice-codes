# brute force :
def findnumappaearingonce(arr):
    for num in arr:
        count=0
        for next_num in arr:
            if num==next_num:
                count+=1
        if count==1:
            return num
arr=[int(x) for x in input().split()]
print(findnumappaearingonce(arr))
#time complexity : O(n^2)

#optimal:
def findnumappearingonce(arr):
    count_dict={}
    for num in arr:
        if num in count_dict:
            count_dict[num]+=1
        else:
            count_dict[num]=1
    for num, count in count_dict.items():
        if count==1:
            return num
arr=[int(x) for x in input().split()]
print(findnumappearingonce(arr))
# time complexity : O(n)

#alternate approach:
def find_single_number(arr):
    result=0
    for num in arr:
        result^=num
    return result
arr=[int(x) for x in input().split()]
print(find_single_number(arr))
# time complexity : O(n)