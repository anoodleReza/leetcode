import math
from typing import List


class Solution:
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True
    def primeSubOperation(self, nums: List[int]) -> bool:
        max_element = max(nums)
        previous_prime = [0] * (max_element+1)

        # find all prime numbers needed
        for i in range (2, max_element):
            if self.is_prime(i):
                previous_prime[i] = i
            else:
                previous_prime[i] = previous_prime[i - 1]

        # check if the difference is ascending
        for i in range(len(nums)):
            if i == 0:
                temp = nums[0]
            else:
                temp = nums[i] - nums[i-1]

            if temp <= 0:
                return False

            largest_prime = previous_prime[temp - 1]
            nums[i] -= largest_prime
        return True
