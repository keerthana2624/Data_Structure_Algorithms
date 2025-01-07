

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

# 4. Check if an array is sorted. 
def check_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
# print(check_sorted([1,2,3,4,5,6]))
# print(check_sorted([1,6,3,4,9,6]))


# 5. Find the sum of all elements in an array.  
def SumOfElements(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum
# print(SumOfElements([2,4,2,5,1,1]))
        
# 6. Count the frequency of each element in an array.  

def countEle(arr):
    count={}
    for i in arr:
        if i in count:
            count[i]+=1
        else: 
            count[i]=1
    return count
# print(countEle([3,2,2,5,5,5]))
# print(countEle([1,2,3,4,5]))


# 7. Remove duplicates from an array. 

def removeDuplicates(arr):
    array=sorted(set(arr))
    for i in range(len(array)-1):
        arr[i]=array[i]
    return array
# print(removeDuplicates([1,2,2,5,3,1]))
        

# 8. Find the index of a given element in an array.

def indexOfEle(arr,n):
    for i in range(len(arr)):
        if arr[i]==n:
            return i
# print(indexOfEle([1,2,2,4,5,4],4))

def indexOfEle(arr,n):
    index=[]
    for i in range(len(arr)):
        if arr[i]==n:
            index.append(i)
    return index
# print(indexOfEle([1,2,2,4,5,4],4))