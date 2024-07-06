class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cur = 1
        while time > 0:
            while cur < n and time > 0:
                cur += 1
                time -= 1
            
            while cur > 1 and time > 0:
                cur -= 1
                time -= 1
        
        return cur
