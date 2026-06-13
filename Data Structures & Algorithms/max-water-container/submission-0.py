class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0

        i = 0
        j = n - 1

        while i < j:
            area = max(area, abs(i - j) * min(heights[i], heights[j]))
            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        
        return area