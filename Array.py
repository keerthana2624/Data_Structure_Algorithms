# 1.Largest Element in the Array

def largestNum(arr):
    largestNum=arr[0]
    for i in arr:
        if i > largestNum:
            largestNum=i
    else:
        return largestNum
# print(largestNum([2,5,3,7]))