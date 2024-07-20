class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x = max(nums)
        y = min(nums)

        for i in range(y, 0, -1):
            if y % i == 0 and x % i == 0:
                return i
