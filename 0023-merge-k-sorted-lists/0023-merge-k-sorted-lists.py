import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Step 1: Push head of each list into the min-heap
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))
        
        dummy = ListNode()
        cur = dummy

        # Step 2: Extract min-heap and build the result
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node # Append current smallest node to the result
            cur = node # Update the cur pointer
            node = node.next # Update the pointer in the corresponding list
            # If there is a valid node, we will push it in the heap
            if node:
                heapq.heappush(heap, (node.val, i,node))
        
        return dummy.next

        # TC: O(N log K)
        # SC: O(K)
            