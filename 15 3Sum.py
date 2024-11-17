from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        if n < 3:
            return ans

        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if cur_sum > 0:
                    r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l_element, r_element = nums[l], nums[r]
                    while l < r and nums[l] == l_element:
                        l += 1
                    while l < r and nums[r] == r_element:
                        r -= 1
        return ans
