class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        h = set()
        
        for n in nums:
            if n in h:
                return True
            else:
                h.add(n)
                
        return False