class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        hm_p, hm_s = {}, {}

        for i in range(len(pattern)):
            if (pattern[i] in hm_p and hm_p[pattern[i]] != words[i]) or (words[i] in hm_s and hm_s[words[i]] != pattern[i]):
                return False

            hm_p[pattern[i]] = words[i]
            hm_s[words[i]] = pattern[i]
        
        return True
