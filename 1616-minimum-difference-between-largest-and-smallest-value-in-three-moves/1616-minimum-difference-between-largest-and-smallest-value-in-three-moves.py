class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        min_four = sorted(heapq.nsmallest(4,nums))
        max_four = sorted(heapq.nlargest(4,nums))

        ans = float("inf")

        for x in range(4):
            ans = min(ans,max_four[x]- min_four[x])
        return ans

