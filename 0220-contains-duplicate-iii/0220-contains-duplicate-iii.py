class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)
        buckets = {}
        numBuckets = valueDiff + 1

        for i in range(n):
            num = nums[i]
            bucketIdx = num // numBuckets

            if bucketIdx in buckets:
                return True
            
            if bucketIdx - 1 in buckets and num - buckets[bucketIdx-1] <= valueDiff:
                return True
            
            if bucketIdx + 1 in buckets and buckets[bucketIdx + 1] - num <= valueDiff:
                return True
            
            buckets[bucketIdx] = num

            if i >= indexDiff:
                del buckets[nums[i-indexDiff] // numBuckets]
        
        return False