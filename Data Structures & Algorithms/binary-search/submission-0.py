class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        u = len(nums)-1

        while l<=u:
            mid = int((u+l)/2)
            print(mid)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                u = mid-1
            elif nums[mid] < target:
                l = mid+1
        
        return -1