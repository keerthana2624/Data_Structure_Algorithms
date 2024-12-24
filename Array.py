# 1.Largest Element in the Array

def largestNum(arr):
    largestNum=arr[0]
    for i in arr:
        if i > largestNum:
            largestNum=i
    else:
        return largestNum
# print(largestNum([2,5,3,7]))

#  2.Second Largest Number
def sec_smallLarge(arr):
    sort=sorted(arr)
    sec_small=sort[1]
    sec_large=sort[-2]
    return(sec_small,sec_large)
# x=[4,2,6,8,99]
# print(sec_smallLarge(x))

#  3.Check Sorted Array

def check_sorted(arr):
    for i in range(len(arr)):
        if arr[i]>arr[i+1]:
            return False
        else:
            return True
# print(check_sorted([4,7,9]))
# print(check_sorted([45,3,9]))

#  Remove Duplicates from Sorted Array
def removeDuplicates(arr):
    new_arr=sorted(set(arr))
    for i in range(len(new_arr)):
        arr[i]=new_arr[i]
    return (len(new_arr))
# print(removeDuplicates([1,2,2,4,5,5]))