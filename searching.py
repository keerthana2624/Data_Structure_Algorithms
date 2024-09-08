# linear search
def Linear(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i 
    return -1
# print(Linear([1,4,2,6],6))
# print(Linear([1,4,2,6],9))
# print(Linear([],4))

