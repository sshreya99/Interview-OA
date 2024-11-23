# warehouse efficiency
# remove first and last element everytime and choose any one for sum. sum should be maximum.
# TC: O(nlogn) SC: O(n)
def solution(arr):
    answer = 0
    heap = []
    left_idx = len(arr)//2 - 1
    right_idx = len(arr)//2
    if len(arr) % 2 != 0:
        answer = arr[right_idx]
        right_idx += 1
    
    while left_idx >= 0 and right_idx < len(arr):
        heapq.heappush(heap, -arr[left_idx])
        heapq.heappush(heap, -arr[right_idx])
        answer += -heapq.heappop(heap)
        left_idx -= 1
        right_idx += 1

    return answer
