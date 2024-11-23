# https://leetcode.com/discuss/interview-question/6008281/Amazon-OA-Newgrad
# TC: O(nlogn) SC: O(n)
from collections import Counter
from heapq import heapify
from heapq import heappop
from heapq import heappush
def optimizeTool(nums):
    count=Counter(nums)
    minheap=list(set(nums))
    heapify(minheap)
    res=[]
    while minheap:
        pop=heappop(minheap)
        if count[pop]<2:
            res.append(pop)
        else:
            pairs=count[pop]//2
            count[pop]-=pairs*2
            if pop*2 not in count:
                heappush(minheap, pop*2)
            count[pop*2]=count.get(pop*2, 0)+pairs
            if count[pop]:
                res.append(pop)
    return res
print(optimizeTool([3, 4, 1, 2, 2, 1, 1]))

# or

def optimizeTool(nums):
    # Create a dictionary to count the frequency of each number
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    # Create a min-heap manually (as a sorted list of unique numbers)
    minheap = sorted(count.keys())
    
    # Result list to store the optimized values
    res = []
    
    while minheap:
        # Simulate popping the smallest element from the min-heap
        pop = minheap.pop(0)
        
        if count[pop] < 2:
            # If less than 2 occurrences, add it to the result
            res.append(pop)
        else:
            # Combine pairs of the current number
            pairs = count[pop] // 2
            count[pop] -= pairs * 2
            
            # Create the doubled value and add it back to the heap if necessary
            new_value = pop * 2
            if new_value not in count:
                minheap.append(new_value)  # Add to heap
                minheap.sort()  # Maintain heap property
            
            # Update the count of the doubled value
            count[new_value] = count.get(new_value, 0) + pairs
            
            # If there's one leftover, add it to the result
            if count[pop]:
                res.append(pop)
    
    return res

# Test the function
print(optimizeTool([3, 4, 1, 2, 2, 1, 1]))
