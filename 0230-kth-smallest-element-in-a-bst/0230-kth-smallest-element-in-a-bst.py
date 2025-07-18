# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [k]
        ans = [0]

        # Using inorder traversal, where we go from left, then root, and then right, that way we can find kth smallest in O(n) time
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            if count[0] == 1:
                ans[0] = node.val
            
            count[0] = count[0] - 1

            if count[0] > 0:
                dfs(node.right)
        
        dfs(root)
        return ans[0]

        # TC: O(n)
        # SC: O(n)