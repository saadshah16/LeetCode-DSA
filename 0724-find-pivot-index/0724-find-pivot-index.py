class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        count = 0

        for i in range(len(nums)):
            count += nums[i]
            if count == summ:
                return i
            summ -= nums[i]
        return -1