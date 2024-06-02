class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # TC : O(n + m)
        # SC : O(n)
        s = set(jewels)
        count = 0

        for stone in stones:
            if stone in s:
                count +=1

        return count