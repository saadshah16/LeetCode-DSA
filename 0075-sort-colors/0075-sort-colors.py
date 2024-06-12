class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)    
        L = 0
        R = n-1
        i = 0
        
        while i <= R:
            if nums[i] == 0:
                nums[L] , nums[i] = nums[i] , nums[L]
                L += 1
            elif nums[i] == 2:
                nums[i], nums[R] = nums[R], nums[i]
                R -= 1
                i -= 1
            i += 1
