class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(int(len(nums))):
            j = target - nums[i]
            if j in nums:
                if i != nums.index(j):
                    if i > nums.index(j):
                        return [nums.index(j), i]
                    return [i, nums.index(j)]