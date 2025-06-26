# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            n = len(queue)
            cur_sum = 0
            for _ in range(n):
                node = queue.popleft()
                cur_sum += node.val

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            avg = float(cur_sum) / float(n)
            ans.append(avg)
        
        return ans

        # TC: O(n)
        # SC: O(n)
