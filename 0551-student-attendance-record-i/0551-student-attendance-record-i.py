class Solution:
    def checkRecord(self, s: str) -> bool:
        count_A = 0
        count_L = 0

        for char in s:
            if char == 'A':
                count_A += 1
                count_L = 0
            elif char == 'L':
                count_L += 1
            else:
                count_L = 0
            
            if count_A == 2 or count_L == 3:
                return False
        
        return True
        
        