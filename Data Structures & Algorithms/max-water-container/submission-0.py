class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0

        for i in range(0, len(heights)):
            for j in range(i, len(heights)):
                h = min([heights[i], heights[j]])
                w = j - i
                mx = max([mx, h * w])
        
        return mx