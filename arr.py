# # arr = [1, 2, 3, 4, 5]
# # print(arr[0])

# # adding element and inserting
# arr.append(6)
# arr.insert(1,0)
# # print(arr)

# # removing element
# arr.remove(0)
# # print(arr)



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


def sortedornot(a):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            return 0
    return 1
print(sortedornot([1,10,3,4,2]))

