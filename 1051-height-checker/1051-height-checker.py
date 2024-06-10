class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)
        n = len(heights)
        count = 0
        
        for i in range(n):
            if s[i] != heights[i]:
                count += 1
        return count