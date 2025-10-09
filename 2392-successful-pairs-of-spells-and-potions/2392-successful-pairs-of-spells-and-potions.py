class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        #n = len(spells)
        #m = len(potions)
        #pairs = [1] * n
        #ctr = 0
        #prod = 1

        #for i in range(n):
        #   for j in range(m):
        #        prod = spells[i] * potions[j]
        #        if prod >= success:
        #            ctr += 1
        #    pairs[i] = ctr
        #    ctr = 0
        
        #return pairs

        # TC: O(n*m) Brute force solutionj
        # SC: O(n)

        # Optimal solution

        potions.sort()
        pairs = []

        for s in spells:
            l = 0
            r = len(potions) - 1
            idx = len(potions)

            while l <= r:
                m = (l+r) // 2
                if s * potions[m] >= success:
                    r = m - 1
                    idx = m
                else:
                    l = m + 1
            
            pairs.append(len(potions)-idx)
        
        return pairs

        # TC: O(n log m) - To run binary search n times
        # + m log m - To sort the potions array





