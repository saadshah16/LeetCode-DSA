class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        res = 0
        colors += colors
        for i in range(n):
            if colors[i] == colors[i+2] and colors[i] != colors[i+1]:
                res += 1
        return res