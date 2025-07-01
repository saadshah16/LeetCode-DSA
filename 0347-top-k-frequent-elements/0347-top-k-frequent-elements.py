class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # Hashmap to count frequency
        freq = [[] for i in range(len(nums)+1)] # Bucket array where the frequency == index

        # Counting the frequency of each number
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        # Grouping numbers by their frequency
        for num,c in count.items():
            freq[c].append(num)
        
        res = []
        # Traverse the bucket array in reverse to get the most frequent elements first
        for i in range(len(nums),0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        # TC: O(n)
        # SC: O(n)