class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_right = [0] * len(s)

        for i in range(len(s)-2,-1,-1):
            a_right[i] = a_right[i+1]
            a_right[i] += 1 if s[i+1] == 'a' else 0
        
        b_left = 0
        res = len(s)
        for i,c in enumerate(s):
            res = min(res,b_left + a_right[i])
            if c == 'b':
                b_left += 1
        
        return res