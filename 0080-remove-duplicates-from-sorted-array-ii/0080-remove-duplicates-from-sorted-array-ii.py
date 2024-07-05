class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L , R = 0, 0
        n = len(nums)

        while R < n:
            count = 1
            while R + 1 < n and nums[R] == nums[R+1]:
                R += 1
                count += 1
            
            for i in range(min(2,count)):
                nums[L] = nums[R]
                L += 1
            R += 1
        return L


    # TC: O(n)
    # SC: O(1)