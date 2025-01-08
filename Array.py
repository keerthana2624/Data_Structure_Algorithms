
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

# 9. Merge two arrays and sort the resulting array. 

def merge_sort(arr1,arr2):
    merged=arr1+arr2
    for i in range(len(merged)):
        for j in range(len(merged)-i-1):
            if merged[j]>merged[j+1]:
                merged[j],merged[j+1]=merged[j+1],merged[j]
    return merged
# print(merge_sort([2,4,6,8],[1,3,5,7]))



# 10. Find the difference between the maximum and minimum elements in an array.
def diffOfMax_Min(arr):
    max=arr[0]
    min=arr[0]
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
        if arr[i]<min:
            min=arr[i]
    return max-min
# print(diffOfMax_Min([2,5,1,8]))



# 11. Count the number of even and odd numbers in an array.  
def evenOdd(array):
    countOfeven=0
    countOfodd=0
    for i in range(len(array)):
        if array[i]%2==0:
            countOfeven+=1
        else:
            countOfodd+=1
    return countOfeven,countOfodd
# print(evenOdd([2,3,6,5,8,1,7]))


# 12. Check if two arrays are equal (contain the same elements in any order). 
def equalArray(arr1,arr2):
    if len(arr1)==len(arr2):
        return True
    else:
        return False
# print(equalArray([1,4,6,3],[7,2,8]))


# 13.Find the common elements in two sorted arrays. 
def commonelement(arr1,arr2):
    common=[]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j]:
                common.append(arr1[i])
    return common
# print(commonelement([1,3,4,6],[2,3,6,7]))
# print(commonelement([2,4,1,6],[3,5,7,9]))



# 14. Find all unique elements in an array. 

def uniqueEle(array):
    unique=[]
    for i in range(len(array)):
        count=0
        for j in range(len(array)):
            if array[i]==array[j]:
                count+=1
        if count==1:
            unique.append(array[i])
    return unique
# print(uniqueEle([1,4,3,1,4,7]))
# print(uniqueEle([1,4,3,1,4,]))


# 15. Find the duplicate elements in an array. 

def duplicate(array):
    dupli=[]
    for i in range(len(array)):
        c=0
        for j in range(len(array)):
            if array[i]==array[j]:
                c+=1
        if c>1 and array[i] not in dupli:
            dupli.append(array[i])
    return dupli
print(duplicate([1,4,2,1,4,1]))
            
