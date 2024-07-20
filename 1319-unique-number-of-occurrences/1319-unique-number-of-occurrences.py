class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = defaultdict(int)
        for i in arr:
            hm[i] += 1
        
        s = set()
        for count in hm.values():
            s.add(count)
        
        return len(s) == len(hm)
        
      
