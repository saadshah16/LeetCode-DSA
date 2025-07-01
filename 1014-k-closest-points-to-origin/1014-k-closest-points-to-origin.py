import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x,y):
            return (x*x)+(y*y)
        
        heap = []
        for x,y in points:
            d = dist(x,y)

            if len(heap) < k:
                heapq.heappush(heap,(-d,x,y))
            else:
                heapq.heappushpop(heap, (-d,x,y))
        
        return [(x,y) for d,x,y in heap]

        # TC: O(n log k)
        # SC: O(k)