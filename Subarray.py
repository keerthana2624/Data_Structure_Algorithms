# Subarray Problems:

# 1.Find the subarray with the maximum sum 

def max_subarray(arr):
    max_sum=float('-inf')
    current_sum=0
    for i in arr:
        current_sum+=i
        if current_sum>max_sum:
            max_sum=current_sum
        if current_sum<0:
            current_sum=0
    return max_sum
# print(max_subarray([-2, -3, 4, -1, -2, 1]))