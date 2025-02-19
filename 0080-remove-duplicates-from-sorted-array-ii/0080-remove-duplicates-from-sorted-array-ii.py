class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        ctr = 1
        n= len(nums)

        for i in range(1,n):
            if nums[i] == nums[i-1]:
                ctr += 1
            else:
                ctr = 1
            
            if ctr <= 2:
                nums[index] = nums[i]
                index += 1
        return index

        # TC: O(n)
        # SC: O(1)