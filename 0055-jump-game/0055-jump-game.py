class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy approach - Start at end
        
        n = len(nums)
        target = n-1
        
        for i in range(n-1,-1,-1):
            max_jump = nums[i]
            
            if i + max_jump >= target:
                target = i
        
        if target == 0:
            return True
        else: return False
        
    # TC: O(n)
    # SC: O(1)