class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        l = 0
        u = n-1

        while l<u:
            s = numbers[l] + numbers[u]

            if s == target:
                return [l+1,u+1]
            elif s > target:
                u -= 1
            else:
                l += 1