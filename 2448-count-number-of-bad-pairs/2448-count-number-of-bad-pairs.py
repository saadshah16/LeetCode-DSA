from collections import defaultdict 
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        gp = 0
        hm = defaultdict(int)

        for i in range(n):
            key = nums[i] - i
            gp += hm[key]
            hm[key] += 1

        tot_pairs = n * (n-1) // 2 
        bad_pairs = tot_pairs - gp
        return bad_pairs

        #TC: O(n)


        
