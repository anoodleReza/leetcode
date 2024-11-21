class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_destination = [0] * n

        if n==1:
            return True

        for i in range(n):
            max_destination[i] = i + nums[i]

        cur_destination = n-1
        for i in range(n-2, -1, -1):
            if max_destination[i] >= cur_destination:
                cur_destination = i
            if cur_destination == 0:
                return True
        return False
