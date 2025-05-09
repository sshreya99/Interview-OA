# truck dock bays

class Solution:
  def getMinimumDockBays(self, truckCargoSize: List[int], maxTurnaroundTime: int) -> int:
    l, r = 1, len(truckCargoSize)

    minD = r
    while l <= r:
      d = l + (r-l) // 2

      # Find total time for selected number of dock bays
      time = 0
      pq = [time] * d
      heapq.heapify(pq)
      for size in truckCargoSize:
        cur = heapq.heappop(pq) + size
        time = max(time, cur)
        heapq.heappush(pq, cur)
      while pq:
        time = max(time, heapq.heappop(pq))

      if time > maxTurnaroundTime:
        l = d + 1
      else:
        r = d - 1
        minD = min(minD, d)

    return minD