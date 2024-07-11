class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        n = len(word1)
        m = len(word2)

        for i in range(min(n,m)):
            res += word1[i] + word2[i]
        
        return res + word1[i+1:] + word2[i+1:]
