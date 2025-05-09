# lexicographically_maximal_resulting_array packages of various weights

from functools import lru_cache
from typing import List

def lexicographically_maximal_resulting_array(k: int, weight: List[int]) -> List[int]:
    n = len(weight)

    @lru_cache(None)
    def dp(i):
        if i >= n:
            return []
        option1 = dp(i + 1)
        option2 = [weight[i]] + dp(i + k + 1)
        return max(option1, option2)

    return dp(0)

k = 2
weight = [10, 5, 9, 2, 5]
print(lexicographically_maximal_resulting_array(k, weight))
