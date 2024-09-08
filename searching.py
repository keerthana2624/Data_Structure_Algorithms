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
        mid=left+(right-left)//2
        if arr[mid]==target:
            return mid
        if target>arr[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1
# print(Binary([1,4,6,8,9,11],8))
# print(Binary([1,4,6,8,9,11],1))
# print(Binary([],8))

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




