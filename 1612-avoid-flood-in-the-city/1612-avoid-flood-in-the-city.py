from sortedcontainers import SortedSet
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [1] * n
        last_rain_day = {}
        dry_days = SortedSet()

        for i in range(n):
            lake = rains[i]

            if lake == 0:
                dry_days.add(i)
            else:
                ans[i] = -1

                if lake in last_rain_day:
                    index = dry_days.bisect_left(last_rain_day[lake]+1)

                    if index == len(dry_days):
                        return []
                    
                    dry_day = dry_days[index]
                    ans[dry_day] = lake
                    dry_days.remove(dry_day)
                
                last_rain_day[lake] = i
        
        return ans

        # TC: O(n log n)
        # SC: O(n)