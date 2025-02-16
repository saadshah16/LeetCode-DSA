class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        cur_sum = max_sum = 0

        for i in range(n):
            if i > 0:
                if nums[i] > nums[i-1]:
                    cur_sum += nums[i]
                    max_sum = max(max_sum,cur_sum)
                else:
                    cur_sum = nums[i]
                    max_sum = max(max_sum,cur_sum)
            else:
                cur_sum = nums[i]
                max_sum = max(max_sum,cur_sum)
            
        
        return max_sum
                
            
