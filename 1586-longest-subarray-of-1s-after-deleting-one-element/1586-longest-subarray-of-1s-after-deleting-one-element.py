class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        L = 0
        R = 1
        count = 0

        for R in range(len(nums)):
            if nums[R] == 0:
                count += 1
            
            while count > 1:
                if nums[L] == 0:
                    count -= 1
                L += 1
            
            res = max(res,R-L)
        
        return res



