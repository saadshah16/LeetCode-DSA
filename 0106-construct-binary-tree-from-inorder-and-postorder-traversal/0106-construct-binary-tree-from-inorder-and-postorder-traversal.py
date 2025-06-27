# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        inorder_hm = {val: idx for idx,val in enumerate(inorder)}

        # Root in postorder will be the last element
        postorder_idx = len(postorder) - 1

        def helper(left: int,right: int) -> Optional[TreeNode]:
            nonlocal postorder_idx

            if left > right:
                return None
            
            # Update current node
            root_val = postorder[postorder_idx]
            postorder_idx -= 1
            root = TreeNode(root_val)

            # Find index in inorder to split the left and right subtrees
            index = inorder_hm[root_val]

            # Recursively build right subtree first, then left subtree
            root.right = helper(index+1,right)
            root.left = helper(left,index-1)

            return root
        
        return helper(0,len(inorder)-1)

        # TC: O(n)
        # SC: O(n)

