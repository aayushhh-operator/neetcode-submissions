class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0

        leftMax = height[0]
        rightMax = height[n-1]

        i = 0
        j = n - 1

        while i < j:
            if leftMax < rightMax:
                i += 1
                leftMax = max(leftMax, height[i])
                result += leftMax - height[i]
            else:
                j -= 1
                rightMax = max(rightMax, height[j])
                result += rightMax - height[j]  

        return result    