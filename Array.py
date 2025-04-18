
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
# print(duplicate([1,4,2,1,4,1]))
            
# 16. Find the missing number in an array containing numbers from 1 to N. 
def missingNum(array,n):
    total_sum=n*(n+1)//2
    sumOfNums=sum(array)
    return sumOfNums-total_sum
# print(missingNum([1,3,6,2,7],5))

# 17. Find the cumulative sum of elements in an array (prefix sum array).
def cumulative(array):
    cumulative_sum=[]
    current_sum=0
    for i in array:
        current_sum+=i
        cumulative_sum.append(current_sum)
    return cumulative_sum
# print(cumulative([1,2,3,4,5]))



# Two Sum (Easy)
def Twosum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return i,j
# print(Twosum([2,5,2,3,3],6))

# Remove Duplicates from Sorted Array (Easy)
def removeDuplicates(arr):
    array=sorted(set(arr))
    for i in range(len(array)-1):
        arr[i]=array[i]
    return array
# print(removeDuplicates([1,2,2,5,3,1]))


# max_subarray
def max_subarray(array):
    max_sum=array[0]
    current_sum=array[0]
    for i in range(1,len(array)):
        current_sum=max(array[i],current_sum+array[i])
        max_sum=max(max_sum,current_sum)
    return max_sum
# print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# merge_sort

def merge_sort(arr1,arr2):
    merged=arr1+arr2
    for i in range(len(merged)):
        for j in range(len(merged)-i-1):
            if merged[j]>merged[j+1]:
                merged[j],merged[j+1]=merged[j+1],merged[j]
    return merged
# print(merge_sort([1,2,3,0,0,0],[2,5,6]))


def merge(a1,a2):
    i=0
    j=0
    merge=[]
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            merge.append(a1[i])
            i+=1
        else:
            merge.append(a2[j])
            j+=1
    while i<len(a1):
        merge.append(a1[i])
        i+=1
    while j<len(a2):
        merge.append(a2[j])
        j+=1
    return merge
# print(merge([1, 2, 3], [2, 5, 6]))


def anagram(string1,string2):
    s1=sorted(string1)
    s2=sorted(string2)
    if s1==s2:
        return True
    else:
        return False
# print(anagram("listen","silent"))



def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def prime_factor(n):
    factor=1
    for i in range(2,n+1):
        if is_prime(i):
            factor*=i
    return factor
n=5
# print(prime_factor(5))


def fibonacci(n):
    a=0
    b=1
    if n<0:
        print("incorrect input")
    elif n==0:
        return 0
    elif n==1:
        return b
    else:
        for i in range(1,n):
            c=a+b
            a=b
            b=c
        return b
# print(fibonacci(9))


def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(9))




# Majority Element

def majority(nums):
    n=len(nums)
    count={}
    for i in nums:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
        if count[i] > n//2:
            return i
# print(majority([3,2,3]))

# remove element

def removeele(nums,val):
    x1=[]
    x2=[]
    c=0
    for i in range(len(nums)):
        if nums[i]==val:
            x1.append(nums[i])
        else:
            x2.append(nums[i])
            c+=1
    return c
# print(removeele([3,2,2,3,3],2))


# Inplace removing element and returning count 
def removeele(nums,val):
    index=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[index]=nums[i]
            index+=1
    return index
# print(removeele([0,1,2,2,3,0,4,2],2))


# removeDuplicates from sorted arr in place
def removeDupli(nums):
    i=0
    for j in range(1,len(nums)):
        if nums[j]!=nums[i]:
            i+=1
            nums[i]=nums[j]
    return nums[:i+1]
# print(removeDupli([1,2,2,4,4]))



# 10/3/25

#1. Find the largest and smallest element in an array.
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

#2. Reverse an array in place.

def reverse_array(arr):
    start = 0
    end = len(arr)-1
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1
    return arr
# print(reverse_array([1,2,3,5,6]))

# 3.Find the second largest element in an array.

# def sec_largest(arr):
#     largest=None
#     second_largest=None
#     for i in arr:
#          if largest is None or i > largest:
#             second_largest=largest
#             largest=i
#     return second_largest



# 4.Check if an array is sorted.

def check_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
# print(check_sorted([1,2,3,4]))
# print(check_sorted([1,2,6,9,4]))



# 5.Remove duplicates from a sorted array.

def remove_dupli(arr):
    j=0
    for i in range(1,len(arr)):
        if arr[i]!=arr[j]:
            j+=1
            arr[j]=arr[i]
    return arr[:j+1]
# print(remove_dupli([1,2,2,3,4,4]))

# >>>>>>>>>>>>>>>>>>>

# 13/3/25


# 1.linear search

def linear(arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            return i
    return -1
# print(linear([1,4,7,3],9))
        


# 2.binary search

def binary(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=left+(right-left)//2
        if arr[mid]==target:
            return mid
        if arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
# print(binary([1,2,6,8],6))


# 3.smallest and largest elements
def smallLarge(arr):
    small=arr[0]
    large=arr[0]
    for i in range(len(arr)-1):
        if arr[i]<small:
            small=arr[i]
        if arr[i]>large:
            large=arr[i]
    return small,large
# print(smallLarge([2,5,8,5,4]))



# 4.majority element from an array

# def majority(arr):
#     count_dict={}
#     for i in arr:
#         if i in count_dict:
#             count_dict[i]+=1
#         else:
#             count_dict[i]=1

#     # return count_dict
#     max=0
#     ans=0
#     for k in count_dict:
#         if count_dict[k] > max:
#             max=count_dict[k]
#             ans=k
#     return ans


def majority(arr):
    count_dic={}
    max=0
    most_frq=None
    for i in arr:
        if i in count_dic:
            count_dic[i]+=1
            if count_dic[i]>max:
                max=count_dic[i]
                most_frq=i
        else:
            count_dic[i]=1
            if count_dic[i]>max:
                max=count_dic[i]
                most_frq=i


    return most_frq
# print(majority([1,4,4,6,6,6,7]))



# 5.merge sorted arrays
def mergeOfsorted(a1,a2):
    i=0
    j=0
    merge=[]
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            merge.append(a1[i])
            i+=1
        else:
            merge.append(a2[j])
            j+=1
    while i<len(a1):
        merge.append(a1[i])
        i+=1
    while j<len(a2):
        merge.append(a2[j])
        j+=1
    return merge
# print(mergeOfsorted([1,2,3,4],[5,6,7,8]))
# print(mergeOfsorted([1,4,5,7],[2,3,6,8]))


# 6.reverse the given array 

def reverseArray(arr):
    start=0
    end=len(arr)-1
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr
# print(reverseArray([1,2,3,4,6]))

# 7.count the frequency of each element in an array

def count_frequency(arr):
    count={}
    for i in arr:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count
# print(count_frequency([1,2,1,6,2,2,7,3,2]))


# 8.finding the missing number in an array

def find_missingNumber(arr):
    n=len(arr)+1
    total_sum=0
    array_sum=0
    for i in range(1,n+1):
        total_sum+=i
    for j in arr:
        array_sum+=j
    return total_sum-array_sum
# print(find_missingNumber([1,3,4,5,6]))



# 9.remove duplicates from sorted array

def remove_dupli_sorted(arr):
    new_array=[arr[0]]
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            new_array.append(arr[i])
    return new_array
# print(remove_dupli_sorted([1,2,2,3,5]))



# 10.calculating the sum of elements in an array

def sum_elements(arr):
    total=0
    for i in arr:
        total+=i
    return total
# print(sum_elements([1,2,3,2,2]))


# find the average of all elements in on array

def average_array(arr):
    total=0
    count=0
    for i in arr:
        total+=i
        count+=1
    return total/count
# print(average_array([1,2,3,4,5]))




# left_rotate
def left_rotate(arr,k):
    n=len(arr)
    k=k%n
    for i in range(k):
        first=arr[0]
        for j in range(n-1):
            arr[j]=arr[j+1]
        arr[n-1]=first
arr=[1,2,3] 
left_rotate(arr,2)
# print(arr)       

# right_rotate
def right_rotate(arr,k):
    n=len(arr)
    k=k%n
    for i in range(k):
        last=arr[n-1]
        for j in range(n-1,0,-1):
            arr[j]=arr[j-1]
        arr[0]=last
arr=[1,2,3] 
right_rotate(arr,2)
# print(arr) 



# def left(a,k):
#     n=len(a)
#     k=k%n
#     for i in range(k):
#         first=a[0]
#         for j in range(n-1):
#             a[j]=a[j+1]
#         a[n-1]=first
# a=[1,2,3,4]
# left(a,2)

# print(a)


# seach for an element in an array


def searching_ele(arr,t):
    for i in range(len(arr)):
        if arr[i]==t:
            return i
        else:
            return 1
# print(searching_ele([22,13,16,38],14))


# # sort the elements of an array by frequency

# def sort_frequency(arr):
#     count={}
#     for i in arr:
#         if i in count:
#             count[i]+=1
#         else:
#             count[i]=1
    
# print(sort_frequency([1,2,1,3,1,5,2,3]))



# selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        small=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[small]:
                small=j
        arr[i],arr[small]=arr[small],arr[i]
    return arr
# print(selection_sort([1,4,2,5,3]))


# insertion sort

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
# print(insertion_sort([1,5,2,6,3,4]))

# merge sort
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    i=0
    j=0
    merged_arr=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merged_arr.append(left[i])
            i+=1
        else:
            merged_arr.append(right[j])
            j+=1
    while i<len(left):
        merged_arr.append(left[i])
        i+=1
    while j<len(right):
        merged_arr.append(right[j])
        j+=1
    return merged_arr
# print(merge_sort([1,4,2,5,9,6,7]))



# Quick_sort

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[]
    right=[]
    for i in range(len(arr)-1):
        if arr[i]<pivot:
            left.append(arr[i])
        elif arr[i]>pivot:
            right.append(arr[i])
    return quick_sort(left)+[pivot]+quick_sort(right)
# print(quick_sort([ 1, 3, 12, 5, 14, 8, 11]))
# print(quick_sort([ 1, 3, 12, 5, 14, 8, 11,2]))


# Fibonacci series

def fibonaci(n):
    a=0
    b=1
    while a<=n:
        print(a,end=' ')
        a,b=b,a+b
# fibonaci(10)

# factorial of n
def factorial(n):
    fact=1
    while n>=1:
        fact=fact*n
        n-=1
    print(fact)
# factorial(5)

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
# print(factorial(n))

# Move All Zeros to End

def move_zero_end(arr):
    a1=[]
    a2=[]
    for i in arr:
        if i!=0:
            a1.append(i)
        else:
            a2.append(i)
    return a1+a2
# print(move_zero_end([1,4,0,3,0,2,5,0]))


# Print All Subarrays of an Array

def subarrays_array(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print(arr[i:j+1])
# subarrays_array([1,2,3,4])

# Buy and Sell Stock

def Max_profit(arr):
    min_price=float('inf')
    Max_profit=0
    for price in arr:
        if price<min_price:
            min_price=price
        elif price-min_price>Max_profit:
            Max_profit=price-min_price
    return Max_profit
# print(Max_profit([7,3,1,9]))




# find the second largest numbers from the given array
def second_largest(arr):
    first=0
    second=0
    for i in arr:
        if i>first:
            second=first
            first=i     
        elif i!=first and i>second:
            second=i
    return second
# print(second_largest([2,7,1,4,9]))


def sum_sub_arr(arr,t):
    Result=[]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sub_arr=arr[i:j+1]
            # print(sub_arr)
            if sum(sub_arr)==t:
                Result.append(sub_arr)
    return Result
# print(sum_sub_arr([1,2,2,2,3,4,2, 7, 6, 4,1,1],7))


