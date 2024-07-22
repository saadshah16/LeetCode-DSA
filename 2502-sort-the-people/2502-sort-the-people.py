class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hm = {}
        for h,n in zip(heights,names):
            hm[h] = n
        
        res = []

        for h in reversed(sorted(heights)):
            res.append(hm[h])

        return res

        # TC : O(n logn)
        # SC: O(n)

            

   
