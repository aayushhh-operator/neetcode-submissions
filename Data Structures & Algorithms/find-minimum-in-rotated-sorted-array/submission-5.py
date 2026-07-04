import math

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        smallest = nums[int((l+r)/2)]

        while l<=r:
            mid = int((l+r)/2)

            if nums[l] <= nums[mid]:
                smallest = min(smallest, nums[l])
                l = mid+1
            elif nums[r] >= nums[mid]:
                smallest = min(smallest, nums[mid])
                r = mid-1

        return smallest