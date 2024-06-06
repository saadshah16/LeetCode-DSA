# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, min, max):
            if not node:
                return True
            
            if node.val <= min or node.val >= max:
                return False
            
            return is_valid(node.left, min, node.val) and is_valid(node.right, node.val, max)
    
        return is_valid(root, float('-inf'), float('inf'))
    
    # TC: O(n)
    # SC: O(h)