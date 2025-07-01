import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Negate the elements, since heapq only uses a min-heap
        for i in range(len(nums)):
            nums[i] = - nums[i]
        
        heapq.heapify(nums)

        for _ in range(k-1):
            heapq.heappop(nums)
            
        
        return -heapq.heappop(nums)

        # TC: O(n + k log n) heapify takes O(n) times, and each of the k pops takes O(n) times
        # SC: O(1)
