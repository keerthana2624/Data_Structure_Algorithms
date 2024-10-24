# linear search
def Linear(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i 
    return -1
# print(Linear([1,4,2,6],6))
# print(Linear([1,4,2,6],9))
# print(Linear([],4))

# binary search

def Binary(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid = left + (right - left) // 2 
        if arr[mid]==target:
            return mid
        if target>arr[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1
print(Binary([1,4,6,8,9,11],8))
print(Binary([1,4,6,8,9,11],1))
print(Binary([],8))

# selection sort

def selectionSort(arr):
    for i in range(len(arr)):
       small=i
       for j in range(i+1,len(arr)):
           if arr[j]<arr[small]:
               small=j
       arr[i], arr[small] = arr[small], arr[i]
    return arr
# print(selectionSort([2,6,3,7,1,9]))


def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left_sorted=mergeSort(left)
    right_sorted=mergeSort(right)
    return merge(left_sorted,right_sorted)

def merge(left,right):
    sorted=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1
    while i<len(left):
        sorted.append(left[i])
        i+=1

    while j < len(right):
        sorted.append(right[j])
        j += 1

    return sorted

# print(mergeSort([2,8,1,5,9,6]))


def searchInsert(nums, target):
     left,right=0,len(nums)-1
     while left<=right:
          mid=(left+right)//2
          if nums[mid]==target:
               return mid
          elif nums[mid]<target:
               left=mid+1
          else:
               right=mid-1
     return left
nums=[2,3,5,7]
target=6
print(searchInsert(nums,target))