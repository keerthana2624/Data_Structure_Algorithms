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


def moveZero(arr):
    