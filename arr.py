# # arr = [1, 2, 3, 4, 5]
# # print(arr[0])

# # adding element and inserting
# arr.append(6)
# arr.insert(1,0)
# # print(arr)

# # removing element
# arr.remove(0)
# # print(arr)


# finding maximum element 
def find_minmax(arr):
    max=arr[0]
    min=arr[0]
    for i in arr:
        if i>max:
            max=i
        if i<min:
            min=i
    return max,min
# arr=[2.4,7,1,9]
# max,min=find_minmax(arr)
# print(f"min:{min},max:{max}")

# arr is sorted or not
def sortedornot(a):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            return 0
    return 1
# print(sortedornot([1,10,3,4,2]))


# removed duplicated from the arr
def removeDuplivates(arr):
    new_arr=sorted(set(arr))
    for i in range(len(new_arr)):
        arr[i]=new_arr[i]
    return new_arr
# print(removeDuplivates([1,3,2,4,3,2]))


# implimented the  left rotateArray
def rotateArray(arr):
    # Write your code from here.
    new_arr=arr[2:]+arr[:2]
    print(new_arr)
# print(rotateArray([1,2,3,4]))


# moved zeros in an array to the end
def movezeros(arr):
#    new=sorted(arr)
#    array=new[2:]+new[:2]
#    print(array)
    result1 = []
    result2=[]
    for num in arr:
        if num != 0:
            result1.append(num)
        if num==0:
            result2.append(num)
    return result1+result2
# print(movezeros([1,2,0,0,0,3]))


# finding the number in the array
def findingNum(arr):
    for i in range(len(arr)):
        if arr[i]==3:
            print(i)
# print(findingNum([1,3,5,3,6]))


def sortedArray(a,b):
    x=a+b
    sort=sorted(set(x))
    print(sort)
# print(sortedArray([1,2,4],[2,3,5]))


def numstriangle(n):
    for i in range(n):
        for j in range(i):
            print(j+i,end='')
        print()
# print(numstriangle(4))


def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def primefactors(n):
    x = 1
    for i in range(2, n + 1):
        if is_prime(i):
            x *= i
    return x
n=5
print(primefactors(n))

def max_product_of_three(nums):
    nums.sort()
    max_product1=nums[-1]*nums[-2]*nums[-3]
    max_product2=nums[0]*nums[1]*nums[-1]
    if max_product1>max_product2:
        return max_product1
    else:
        return max_product2
# n=[2,4,1,5,6]
# print(max_product_of_three(n))



def subset_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False
# print(subset_sum([3,1,1,4,8,5],5))




# Remove Element
def removeElement(nums, val):
    elements=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[elements]=nums[i]
            elements+=1
    return elements
nums=[0,1,2,2,3,0,4,2]
val=2
# print(removeElement(nums,val))


# Remove Duplicates from Sorted Array
def removeduplicates(nums):
    count=0
    for i in range(1,len(nums)):
        if nums[i]!=nums[count]:
            count+=1
            nums[count]=nums[i]
    return count+1
nums=[0,0,1,1,1,2,2,3,3]
# print(removeduplicates(nums))


# Majority Element
def majorityelement(nums):
    d={}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for j in d:
        if d[j]>len(nums)/2:
            return j
    return -1
nums=[3,2,3,2,2]
print(majorityelement(nums))



