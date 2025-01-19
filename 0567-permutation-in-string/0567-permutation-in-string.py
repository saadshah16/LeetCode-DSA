class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = [0] * 26
        s2_counts = [0] * 26
        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i])- 97] += 1

        if  s2_counts == s1_counts:
                return True
        
        for i in range(len(s1), len(s2)):
            s2_counts[ord(s2[i]) - 97] += 1
            s2_counts[ord(s2[i-len(s1)]) - ord('a')] -= 1

            if s2_counts == s1_counts:
                return True
        
        return False