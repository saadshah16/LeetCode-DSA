class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []

        for i,n in enumerate(nums):
            mapped_n = 0
            if n == 0:
                mapped_n = mapping[n]
            base = 1
            while n > 0:
                digit = n % 10
                n = n // 10
                mapped_n += base * mapping[digit]
                base *= 10
            pairs.append((mapped_n,i))
        
        pairs.sort()
        return [nums[p[1]] for p in pairs]