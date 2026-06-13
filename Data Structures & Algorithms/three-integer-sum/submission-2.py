class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        n = len(nums)

        nums.sort()

        for i in range(n):
            temp = 0 - nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                    s = nums[j] + nums[k]

                    if s == temp:
                        output.add((nums[i], nums[j], nums[k]))
                        j += 1
                        k -= 1
                    elif s > temp:
                        k -= 1
                    else:
                        j += 1
        
        return list(output)