from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        count_map = defaultdict(int)
        rem = []
        res = []

        for num in arr2:
            count_map[num] = 0

        for num in arr1:
            if num in count_map:
                count_map[num] += 1
            else:
                rem.append(num)
        
        rem.sort()

        for num in arr2:
            res.extend([num]*count_map[num])
        res.extend(rem)

        return res
        