class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        moves = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= prev:
                prev += 1
                moves += prev - nums[i]
            else:
                prev = nums[i]
        return moves
