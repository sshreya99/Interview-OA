# Get Total Requests - amazon servers

class Solution:
  def getTotalRequests(self, server: List[int], replaced: List[int], newId: List[int]) -> List[int]:
    ans = []
    for j in range(len(replaced)):
      for i in range(len(server)):
        if server[i] == replaced[j]:
          server[i] = newId[j]
      ans.append(sum(server))
    return ans