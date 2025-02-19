class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Better solution using two pointers for o(1) sc
        j = 0

        for i in range(1,len(nums)):
            if nums[j] != nums[i]:
                j+= 1
                nums[j] = nums[i]
        return j+1





        #hm = {}
        #n = len(nums)
        #k = 0

        #for i in range(n):
         #   if nums[i] not in hm.values():
          #      hm[i] = nums[i]
           #     nums[k] = nums[i]
            #    k += 1
            #else:
             #   continue
        
       # return k

            # TC: O(n)
            # SC: O(n)
        
