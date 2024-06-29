class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n-1,-1,-1):
            if s[i] != " ":
                res += 1
            elif res:
                return res
        
        return res
            
