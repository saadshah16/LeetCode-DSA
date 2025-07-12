# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 1
        que = deque()
        que.append(root)
        level = 1
        max_sum = float('-inf')
        max_level = 1

        while que:
            n = len(que)
            cur_sum = 0
            for _ in range(n):
                node = que.popleft()
                cur_sum += node.val
                if node:
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_level = level
            level += 1

        return max_level

# TC: O(n)
# SC: O(w) # Width of the tree