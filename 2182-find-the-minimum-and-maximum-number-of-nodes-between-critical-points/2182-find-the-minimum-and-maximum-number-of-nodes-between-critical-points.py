# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def critical(prev,cur,next):
            return (prev.val < cur.val > next.val or prev.val > cur.val < next.val)

        
        prev,cur = head , head.next
        next = cur.next
        min_dist, max_dist = float('inf'), -1
        i = 1 # Index of cur
        first_crit_index = 0
        prev_crit_index = 0

        while next:
            if critical(prev,cur,next):
                if first_crit_index:
                    max_dist = i - first_crit_index
                    min_dist = min(min_dist,i - prev_crit_index)
                else:
                    first_crit_index = i
                prev_crit_index = i

            prev , cur, next = cur, next , next.next
            i += 1
        
        if min_dist == float('inf'):
            min_dist = -1
        
        return [min_dist,max_dist]