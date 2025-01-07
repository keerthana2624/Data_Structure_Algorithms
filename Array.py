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




# 1. Find the largest and smallest elements in an array.  
def LargSmall(arr):
    larg=arr[0]
    small=arr[0]
    for i in arr:
        if i>larg:
            larg=i
        if i<small:
            small=i
    return larg,small
# print(LargSmall([2,6,3,7]))
# print(LargSmall([0,0,1,0,0]))


# 2. Reverse an array.  

# inplce
def reverse(arr):  
    arr.reverse()
    return arr
# print(reverse([1,3,6,2,4]))
# print(reverse([2,4,5,6,7]))

def reverse(array):
    arr=[]
    for i in range(len(array)-1,-1,-1):
        arr.append(array[i])
    return arr
# print(reverse([3,1,6,4,7]))
# print(reverse([]))
# print(reverse([1,2,3,4,5]))


# 3. Find the second largest element in an array
def sec_large(array):
    array.sort()
    return array[-2]
# print(sec_large([2,4,1,7,5]))