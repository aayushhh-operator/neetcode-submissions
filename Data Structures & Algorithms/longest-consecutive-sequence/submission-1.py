class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        streak = 0
        lcs = 0

        if len(nums) == 0:
            return 0

        small = min(nums)
        large = max(nums)

        for i in range(small, large+1):
            if i in nums:
                streak += 1
                if streak > lcs:
                    lcs = streak
            else:
                streak = 0

        if streak > lcs:
            return streak

        return lcs