class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = 0
        hm = {}
        
        for item in arr:
            if item in hm:
                hm[item] = False
            else:
                hm[item] = True
        
        for item in arr:
            if hm[item]:
                count += 1
            if count == k:
                return item
        
        return ""
            

