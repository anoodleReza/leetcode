from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums) + 1
        prefixSums = [0] * n

        for i in range(1, n):
            prefixSums[i] = prefixSums[i - 1] + nums[i - 1]

        candidates = deque()
        shortest = float("inf")

        for i in range(n):
            while candidates and prefixSums[i] - prefixSums[candidates[0]] >= k:
                shortest = min(shortest, i - candidates.popleft())
            while candidates and prefixSums[i] <= prefixSums[candidates[-1]]:
                candidates.pop()
            candidates.append(i)

        return shortest if shortest != float("inf") else -1



