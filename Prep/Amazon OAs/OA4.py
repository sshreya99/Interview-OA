
# https://leetcode.com/discuss/interview-question/6061550/Amazon-SDE-1-Online-Assessment-Question-with-detailed-explainations
# max sum of subarray:
# TC: 0(n), SC: O(1)

def findMaxSum(arr, k):
    if arr is None or len(arr) == 0 or k > len(arr) or k <= 0:
        return -1
        
    total_sum = sum(arr)
    subarray_sum = sum(arr[:k]) 
    max_sum = subarray_sum   
    
    for i in range(k,len(arr)):
        subarray_sum = subarray_sum + arr[i] - arr[i-k]
        max_sum = max(subarray_sum,max_sum)
    
    return total_sum - max_sum 
     
arr=[5, 3, 9, 7, 4, 1, 8];
print(findMaxSum(arr, 3))
