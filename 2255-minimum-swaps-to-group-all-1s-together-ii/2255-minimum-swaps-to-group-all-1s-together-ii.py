class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = nums.count(1)
        max_ones = 0
        window_ones = 0
        l = 0

        for r in range(2*n):
            if nums[r%n] == 1:
                window_ones += 1
            if r - l + 1 > total_ones:
                window_ones -= nums[l%n]
                l += 1
            max_ones = max(max_ones,window_ones)
        
        return total_ones - max_ones

