class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maximum = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                n = stack.pop()
                left = stack[-1] if stack else -1
                width = i - left - 1
                maximum = max(maximum, (width * heights[n]))
            stack.append(i)
 
        return maximum