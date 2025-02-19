class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hm = {}
        n = len(nums)
        k = 0

        for i in range(n):
            if nums[i] not in hm.values():
                hm[i] = nums[i]
                nums[k] = nums[i]
                k += 1
            else:
                continue
        
        return k

            # TC: O(n)
            # SC: O(n)
        
